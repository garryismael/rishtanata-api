from pydantic_settings import BaseSettings, SettingsConfigDict


class AppConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env.local", env_file_encoding="utf-8")

    db_url: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int
    website_url: str
    mail_username: str
    mail_password: str
    mail_from: str
    mail_port: int
    mail_server: str
    mail_from_name: str


APP_CONFIG = AppConfig()
