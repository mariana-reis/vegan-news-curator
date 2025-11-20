import json
import urllib.request
import urllib.error
import time
import logging
from typing import List, Dict
from config import GNewsConfig

logger = logging.getLogger(__name__)


class NewsCollector:
    MAX_RETRIES = 3
    RETRY_DELAY = 2
    TIMEOUT = 10

    def __init__(self, config: GNewsConfig):
        self.config = config
        self.logger = logger

    def collect(self) -> List[Dict[str, str]]:
        articles = []

        for category in self.config.categories:
            category_articles = self._collect_category(category)
            articles.extend(category_articles)

        return self._remove_duplicates(articles)

    def _collect_category(self, category: str) -> List[Dict[str, str]]:
        for attempt in range(1, self.MAX_RETRIES + 1):
            try:
                self.logger.info(f"Coletando {category} (tentativa {attempt}/{self.MAX_RETRIES})")
                articles = self._fetch_category(category)
                self.logger.info(f"{len(articles)} artigos coletados de {category}")
                return articles

            except urllib.error.HTTPError as e:
                if e.code == 429:
                    self._handle_rate_limit(attempt)
                else:
                    self.logger.error(f"Erro HTTP {e.code} ao coletar {category}")
                    return []

            except Exception as e:
                self.logger.error(f"Erro ao coletar {category}: {str(e)}")
                if attempt < self.MAX_RETRIES:
                    self._wait_before_retry(attempt)
                else:
                    return []
        return []

    def _fetch_category(self, category: str) -> List[Dict[str, str]]:
        params = self._build_params(category)
        url = f"{self.config.base_url}?{params}"

        with urllib.request.urlopen(url, timeout=self.TIMEOUT) as response:
            data = json.loads(response.read().decode("utf-8"))

            if "articles" not in data:
                self.logger.warning(f"Nenhum artigo na resposta de {category}")
                return []

            return self._parse_articles(data["articles"])

    def _build_params(self, category: str) -> str:
        return f"category={category}&lang=en&max=6&q=vegan&apikey={self.config.api_key}"

    def _parse_articles(self, articles_data: List[Dict]) -> List[Dict[str, str]]:
        parsed = []

        for article in articles_data:
            parsed_article = {
                "title": article.get("title", ""),
                "description": article.get("description", ""),
                "content": article.get("content", ""),
                "url": article.get("url", ""),
                "source": article.get("source", {}).get("name", "Desconhecida"),
                "country": article.get("source", {}).get("country", "Global"),
                "published_at": article.get("publishedAt", ""),
            }

            if parsed_article["title"]:  # Apenas artigos com título
                parsed.append(parsed_article)

        return parsed

    def _remove_duplicates(self, articles: List[Dict]) -> List[Dict]:
        unique = []
        seen_urls = set()

        for article in articles:
            url = article["url"]

            if url not in seen_urls:
                unique.append(article)
                seen_urls.add(url)

        return unique[:20]

    def _handle_rate_limit(self, attempt: int) -> None:
        wait_time = self.RETRY_DELAY * (2 ** (attempt - 1))
        self.logger.warning(f"Rate limit detectado. Aguardando {wait_time}s antes de retry...")
        time.sleep(wait_time)

    def _wait_before_retry(self, attempt: int) -> None:
        wait_time = self.RETRY_DELAY * attempt
        self.logger.info(f"Aguardando {wait_time}s antes da tentativa {attempt + 1}...")
        time.sleep(wait_time)