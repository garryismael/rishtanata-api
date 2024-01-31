import io
from deta import Deta

from src.config.app import AppConfig


class UploadService:
    def __init__(self, config: AppConfig) -> None:
        self.deta = Deta(config.deta_project_key)
        self.config = config

    def upload(self, filename: str, data: io.BufferedIOBase):
        self.deta.Drive(filename).put(
            filename,
            data,
        )
