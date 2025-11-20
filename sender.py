import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import EmailConfig


class EmailSender:
    def __init__(self, config: EmailConfig):
        self.config = config
    
    def send(self, subject: str, html_body: str) -> bool:
        if not self._validate():
            return False
        try:
            message = self._build_message(subject, html_body)
            self._send_smtp(message)
            return True
        except Exception as e:
            print(f"Erro ao enviar email: {e}")
            return False
    
    def _validate(self) -> bool:
        if not self.config.sender or not self.config.password:
            print("Erro: EMAIL_SENDER ou EMAIL_PASSWORD nao configurados")
            return False
        return True
    
    def _build_message(self, subject: str, html_body: str) -> MIMEMultipart:
        message = MIMEMultipart("alternative")
        message["Subject"] = subject
        message["From"] = self.config.sender
        message["To"] = self.config.recipient
        
        text_part = MIMEText("Visualize em HTML", "plain")
        message.attach(text_part)
        
        html_part = MIMEText(html_body, "html")
        message.attach(html_part)
        
        return message
    
    def _send_smtp(self, message: MIMEMultipart) -> None:
        with smtplib.SMTP(self.config.smtp_server, self.config.smtp_port) as server:
            server.starttls()
            server.login(self.config.sender, self.config.password)
            server.sendmail(self.config.sender, self.config.recipient, message.as_string())