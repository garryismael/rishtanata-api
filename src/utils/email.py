from pathlib import Path
from typing import Any

from fastapi_mail import ConnectionConfig, FastMail, MessageSchema, MessageType

from src.config.app import AppConfig


class MailService:
    def __init__(self, config: AppConfig) -> None:
        conf = ConnectionConfig(
            MAIL_USERNAME=config.mail_username,
            MAIL_PASSWORD=config.mail_password,
            MAIL_FROM=config.mail_from,
            MAIL_PORT=config.mail_port,
            MAIL_SERVER=config.mail_server,
            MAIL_STARTTLS=True,
            MAIL_SSL_TLS=False,
            TEMPLATE_FOLDER=Path(__file__).parent.parent.parent / "templates",
        )
        self.fast_mail = FastMail(conf)

    async def send(self, subject: str, body: dict[str, Any], template_name: str):
        message = MessageSchema(
            subject=subject,
            recipients=body.get("emails"),
            template_body=body,
            subtype=MessageType.html,
        )
        # await self.fast_mail.send_message(message, template_name=template_name)
