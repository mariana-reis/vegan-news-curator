import re
import logging
from typing import List, Dict

logger = logging.getLogger(__name__)


class ArticleFormatter:
    @staticmethod
    def format_for_agent(articles: List[Dict[str, str]]) -> str:
        output = "NOTICIAS SOBRE VEGANISMO DO MUNDO:\n" + "=" * 80 + "\n\n"

        for index, article in enumerate(articles, 1):
            output += ArticleFormatter._format_single_article(article, index)
        return output

    @staticmethod
    def _format_single_article(article: Dict[str, str], index: int) -> str:
        formatted = f"NOTICIA {index}:\n"
        formatted += f"Titulo: {article['title']}\n"
        formatted += f"Descricao: {article['description']}\n"

        if article.get('content'):
            content_preview = article['content'][:200]
            formatted += f"Conteudo: {content_preview}\n"

        formatted += f"Fonte: {article['source']} | Pais: {article['country']}\n"
        formatted += f"URL: {article['url']}\n"
        formatted += "-" * 80 + "\n\n"

        return formatted


class MarkdownConverter:
    @staticmethod
    def to_html(content: str) -> str:
        html = content

        html = MarkdownConverter._convert_markdown_headers(html)
        html = MarkdownConverter._convert_markdown_bold(html)
        html = MarkdownConverter._convert_markdown_italic(html)
        html = MarkdownConverter._wrap_paragraphs(html)

        return html

    @staticmethod
    def _convert_markdown_headers(html: str) -> str:
        html = re.sub(r'^## (.+)$', r'<h2 style="font-size:20px;font-weight:700;margin:30px 0 15px 0;border-bottom:2px solid #000;padding-bottom:8px">\1</h2>', html, flags=re.MULTILINE)
        return html

    @staticmethod
    def _convert_markdown_bold(html: str) -> str:
        html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html)
        return html

    @staticmethod
    def _convert_markdown_italic(html: str) -> str:
        html = re.sub(r'\*(.+?)\*', r'<em>\1</em>', html)
        return html

    @staticmethod
    def _wrap_paragraphs(html: str) -> str:
        lines = html.split('\n')
        result = []

        for line in lines:
            stripped = line.strip()

            if not stripped:
                result.append(line)
                continue

            if MarkdownConverter._is_html_tag(stripped):
                result.append(line)
                continue

            if MarkdownConverter._is_section_marker(stripped):
                result.append(line)
                continue

            result.append(f'<p style="font-size:13px;line-height:1.8;text-align:justify;margin-bottom:12px;color:#333">{line}</p>')

        return '\n'.join(result)

    @staticmethod
    def _is_html_tag(text: str) -> bool:
        return text.startswith('<') or text.startswith('|')

    @staticmethod
    def _is_section_marker(text: str) -> bool:
        return text.startswith('---') or text.startswith('###')