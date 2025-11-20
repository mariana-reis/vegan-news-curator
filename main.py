import asyncio
from dotenv import load_dotenv

load_dotenv()

from config import AppConfig
from collector import NewsCollector
from converters import ArticleFormatter, MarkdownConverter
from generator import NewsletterGenerator
from sender import EmailSender
from email_template import EmailTemplate


class Application:
    def __init__(self):
        self.config = AppConfig()
    
    async def run(self):
        is_valid, errors = self.config.validate()
        
        if not is_valid:
            print(f"Erro: Variaveis de ambiente faltando: {', '.join(errors)}")
            return
        
        print("🌱 Iniciando coleta de noticias...")
        
        collector = NewsCollector(self.config.gnews)
        articles = collector.collect()
        
        if not articles:
            print("Erro: Nenhum artigo encontrado")
            return
        
        print(f"Coletados {len(articles)} artigos")
        
        articles_text = ArticleFormatter.format_for_agent(articles)
        
        print("🌱 Gerando newsletter com Azure AI...")
        
        generator = NewsletterGenerator(self.config.azure)
        newsletter_content = await generator.generate(articles_text)
        
        print("🌱 Convertendo para HTML...")
        
        html_content = MarkdownConverter.to_html(newsletter_content)
        html_body = EmailTemplate.build(html_content)
        
        print("🌱 Enviando email...")
        
        sender = EmailSender(self.config.email)
        success = sender.send("🌱 Vegan News - Newsletter Semanal", html_body)
        
        if success:
            print("🌱 Email enviado com sucesso")
        else:
            print("Erro ao enviar email")


async def main():
    app = Application()
    await app.run()

if __name__ == "__main__":
    asyncio.run(main())