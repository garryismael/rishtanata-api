from datetime import datetime, timedelta, timezone
from typing import Union

from jose import jwt

from src.config.app import APP_CONFIG


class AccessTokenFactory:
    def create_access_token(
        self, data: dict, expires_delta: Union[timedelta, None] = None
    ):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        else:
            expire = datetime.now(timezone.utc) + timedelta(minutes=480)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(
            to_encode, APP_CONFIG.secret_key, algorithm=APP_CONFIG.algorithm
        )
        return encoded_jwt
