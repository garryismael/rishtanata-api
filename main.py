from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from src.config.app import APP_CONFIG
from src.config.container import Container
from src.routers.user import user_router
from src.routers.account import account_router
from src.routers.auth import auth_router


def create_app() -> FastAPI:
    container = Container()

    api = FastAPI(title="Rish Tanata APP")
    api.container = container
    api.include_router(user_router)
    api.include_router(account_router)
    api.include_router(auth_router)
    return api


app = create_app()


TORTOISE_ORM = {
    "connections": {"default": APP_CONFIG.db_url},
    "apps": {
        "models": {
            "models": ["src.models.user", "src.models.account", "aerich.models"],
            "default_connection": "default",
        },
    },
}

register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=True,
    add_exception_handlers=True,
)