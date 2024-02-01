from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise

from src.config.app import APP_CONFIG
from src.config.container import Container
from src.routers.auth import auth_router
from src.routers.user import user_router


def create_app() -> FastAPI:
    container = Container()

    api = FastAPI(title="Rish Tanata APP")

    api.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    api.container = container
    api.include_router(user_router)
    api.include_router(auth_router)
    return api


app = create_app()

TORTOISE_ORM = {
    "connections": {
        "default": APP_CONFIG.db_url
    },
    "apps": {
        "models": {
            "models": ["src.models.user", "src.models.information", "aerich.models"],
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
