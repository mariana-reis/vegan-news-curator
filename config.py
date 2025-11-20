import os
import logging
from dataclasses import dataclass
from typing import List, Tuple

logger = logging.getLogger(__name__)


@dataclass
class GNewsConfig:    
    api_key: str = os.getenv("GNEWS_API_KEY", "")
    base_url: str = "https://gnews.io/api/v4/top-headlines"
    categories: List[str] = None

    def __post_init__(self) -> None:
        if self.categories is None:
            self.categories = ["health", "business", "science", "world", "technology"]

    def is_valid(self) -> bool:
        return bool(self.api_key)


@dataclass
class AzureConfig:
    project_endpoint: str = os.getenv("AZURE_AI_PROJECT_ENDPOINT", "")
    agent_id: str = os.getenv("AGENT_ID", "")
    model_deployment_name: str = os.getenv("AZURE_AI_MODEL_DEPLOYMENT_NAME", "")
    email_connection_string: str = os.getenv("AZURE_EMAIL_CONNECTION_STRING", "")
    sender_email: str = os.getenv("SENDER_EMAIL", "")

    def is_valid(self) -> bool:
        return bool(
            self.project_endpoint
            and self.agent_id
            and self.model_deployment_name
        )

    def validate_email_config(self) -> bool:
        return bool(self.email_connection_string and self.sender_email)


@dataclass
class EmailConfig:
    sender: str = os.getenv("EMAIL_SENDER", "")
    password: str = os.getenv("EMAIL_PASSWORD", "")
    smtp_server: str = os.getenv("SMTP_SERVER", "smtp.gmail.com")
    smtp_port: int = int(os.getenv("SMTP_PORT", "587"))
    recipient: str = os.getenv("RECIPIENT_EMAIL", "")

    def is_valid(self) -> bool:
        return bool(self.sender and self.password and self.recipient)


@dataclass
class AppConfig:
    gnews: GNewsConfig = None
    azure: AzureConfig = None
    email: EmailConfig = None

    def __post_init__(self) -> None:
        if self.gnews is None:
            self.gnews = GNewsConfig()
        if self.azure is None:
            self.azure = AzureConfig()
        if self.email is None:
            self.email = EmailConfig()

    def _validate_gnews(self) -> List[str]:
        errors = []
        if not self.gnews.is_valid():
            errors.append("GNEWS_API_KEY")
        return errors

    def _validate_azure(self) -> List[str]:
        errors = []
        if not self.azure.is_valid():
            if not self.azure.project_endpoint:
                errors.append("AZURE_AI_PROJECT_ENDPOINT")
            if not self.azure.agent_id:
                errors.append("AGENT_ID")
            if not self.azure.model_deployment_name:
                errors.append("AZURE_AI_MODEL_DEPLOYMENT_NAME")
        return errors

    def _validate_email(self) -> List[str]:
        errors = []
        if not self.email.is_valid():
            if not self.email.sender:
                errors.append("EMAIL_SENDER")
            if not self.email.password:
                errors.append("EMAIL_PASSWORD")
            if not self.email.recipient:
                errors.append("RECIPIENT_EMAIL")
        return errors

    def validate(self) -> Tuple[bool, List[str]]:
        errors = []
        errors.extend(self._validate_gnews())
        errors.extend(self._validate_azure())
        errors.extend(self._validate_email())
        is_valid = len(errors) == 0
        return is_valid, errors

    def log_config_status(self) -> None:
        logger.info("Status das Configurações:")
        logger.info(f"GNews API: {'Configurado' if self.gnews.is_valid() else 'Faltando'}")
        logger.info(f"Azure AI: {'Configurado' if self.azure.is_valid() else 'Faltando'}")
        logger.info(f"Email: {'Configurado' if self.email.is_valid() else 'Faltando'}")

        if self.azure.validate_email_config():
            logger.info(f"Azure Communication Services: Configurado")
        else:
            logger.warning(f"Azure Communication Services: Não configurado")