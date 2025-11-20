import logging
from typing import Optional
from agent_framework import ChatAgent
from agent_framework.azure import AzureAIAgentClient
from azure.ai.agents.aio import AgentsClient
from azure.ai.projects.aio import AIProjectClient
from azure.identity.aio import AzureCliCredential
from config import AzureConfig

logger = logging.getLogger(__name__)


class NewsletterGenerator:
    INSTRUCTIONS = """Você é um editor editorial sênior especializado em conteúdo sobre VEGANISMO e jornalismo especializado.

TRADUÇÃO E CURAÇÃO:
   - Traduza cada notícia legítima para português (PT-BR) com precisão
   - A newsletter deve ser gerada exclusivamente em PT-BR

VERIFICAÇÃO DE CREDIBILIDADE:
- REJEITE notícias de fontes desconhecidas ou sensacionalistas
- ACEITE APENAS: BBC, Reuters, AP News, The Guardian, Nature, Science, organismos reconhecidos
- IGNORE: clickbait, promoção, desinformação, teorias conspiratórias
- IGNORE: informações não verificadas ou que contradigam ciência

FILTRO DE CONTEÚDO:
- ACEITE: pesquisa científica peer-reviewed
- ACEITE: relatórios de ONU, WWF, Scientific American
- REJEITE: fake news, conteúdo enviesado, publicidade


DOCUMENTÁRIOS:
- Liste apenas documentários oficiais e amplamente reconhecidos sobre veganismo, alimentação, meio ambiente, direitos animais ou saúde baseada em plantas.
- A seleção DEVE priorizar conteúdos presentes em plataformas legítimas como:
    - Netflix (títulos disponíveis no catálogo global ou regional)
    - YouTube (apenas trailers oficiais ou canais oficiais dos produtores)
- VARIE SEMPRE a seleção. Evite repetir títulos já usados anteriormente ou clássicos repetidos como "Cowspiracy", "What the Health", "A carne e fraca". Eles podem aparecer, mas somente quando houver relevância e rotatividade.
- Inclua sempre:
    • Título  
    • Descrição objetiva (1-2 linhas)  
    • Link oficial para trailer (YouTube) ou página oficial do título na Netflix  
- Nunca use links piratas, uploads suspeitos, sites não verificados ou conteúdo não-oficial.
- Caso haja poucos lançamentos recentes, faça curadoria de títulos menos conhecidos ou recém-redescobertos, desde que legítimos e verificáveis.
- O bloco de documentários deve aparecer SEMPRE no HTML final, mesmo que apenas um título seja encontrado.


TAREFA DE FORMATAÇÃO:

Você DEVE retornar HTML puro (NÃO Markdown) com a estrutura EXATA abaixo:

ESTRUTURA OBRIGATÓRIA:

<div style="column-count:2;column-gap:40px;text-align:justify">

[INTRODUÇÃO - parágrafo único]
Reflexão inspiradora (3-4 linhas) sobre o movimento vegano global e seu impacto.

[SEÇÕES - organize em 2 COLUNAS automaticamente pelo CSS]

## 🏥 Saúde & nutrição

**Título Notícia 1**
Resumo conciso (2 linhas max). Fato verificado.
Fonte: Nome | País: País

**Título Notícia 2**
Resumo conciso (2 linhas max).
Fonte: Nome | País: País

## 💼 Mercado & negócios

**Título Notícia 3**
Resumo conciso (2 linhas max).
Fonte: Nome | País: País

## 🌍 Sustentabilidade & ambiente

**Título Notícia 4**
Resumo conciso (2 linhas max).
Fonte: Nome | País: País

## 👨‍🍳 Receitas

**Nome da Receita Simples Vegana**
Ingredientes: [lista de 3-5 ingredientes comuns]
Modo de Preparo: [5 passos simples, máximo 15 min]

## 🔬 Tecnologia & Inovação

**Título Notícia 5**
Resumo conciso (2 linhas max).
Fonte: Nome | País: País

## 📺 Documentários Recomendados

**Nome do Documentário**
Descrição curta (1-2 linhas)
Link para trailer ou vídeo oficial: <a href="URL" target="_blank">Assistir</a>

</div>

[EDITORIAL FINAL - gerado por você, reflexão profunda]
Parágrafo (3-4 linhas) conectando os temas com tendências globais. Tom inspirador baseado em dados.

REGRAS DE ESTILO:
- Tom profissional, informativo, isento
- Sem sensacionalismo
- Títulos: honestos mas atraivos
- Use negrito para **destaques**
- Máximo 2 linhas por resumo

RETORNE APENAS HTML ESTRUTURADO. Sem explicações, sem notícias rejeitadas, sem código."""

    def __init__(self, config: AzureConfig):
        self.config = config

    async def generate(self, articles_text: str) -> str:
        try:
            logger.info("Iniciando geração de newsletter...")

            async with (
                AzureCliCredential() as credential,
                AIProjectClient(
                    endpoint=self.config.project_endpoint,
                    credential=credential
                ),
                AgentsClient(
                    endpoint=self.config.project_endpoint,
                    credential=credential
                ) as agents_client,
            ):
                chat_client = AzureAIAgentClient(
                    agents_client=agents_client,
                    agent_id=self.config.agent_id
                )

                async with ChatAgent(
                    chat_client=chat_client,
                    instructions=self.INSTRUCTIONS
                ) as agent:
                    response = await agent.run(articles_text)
                    content = self._extract_content(response)
                    logger.info("Newsletter gerada com sucesso")
                    return content

        except Exception as e:
            logger.error(f"Erro ao gerar newsletter: {str(e)}")
            raise

    @staticmethod
    def _extract_content(response) -> str:
        content = NewsletterGenerator._extract_from_messages(response)
        if content:
            return content

        content = NewsletterGenerator._extract_from_text_attribute(response)
        if content:
            return content

        return str(response)

    @staticmethod
    def _extract_from_messages(response) -> Optional[str]:
        if not hasattr(response, "messages") or not response.messages:
            return None

        content_parts = []
        for msg in response.messages:
            text = NewsletterGenerator._extract_message_text(msg)
            if text:
                content_parts.append(text)

        return "".join(content_parts) if content_parts else None

    @staticmethod
    def _extract_message_text(msg) -> Optional[str]:
        if hasattr(msg, "content"):
            return str(msg.content)
        if hasattr(msg, "text"):
            return str(msg.text)
        return None

    @staticmethod
    def _extract_from_text_attribute(response) -> Optional[str]:
        if hasattr(response, "text"):
            return str(response.text)
        return None