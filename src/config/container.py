from dependency_injector import containers, providers

from src.config.app import AppConfig
from src.domain.auth.use_case import UserLoginUseCase
from src.domain.user.use_case import AccountCreationUseCase, UserRegisterUseCase
from src.models.user.repository import UserRepository
from src.models.user.service import UserService
from src.utils import ApiException
from src.utils.auth import AuthService
from src.utils.email import MailService
from src.utils.token import UserTokenService
from src.utils.token.factory import AccessTokenFactory


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "src.routers.user",
            "src.routers.account",
            "src.routers.auth",
            "src.utils.token",
        ]
    )
    config = providers.Configuration(yaml_files=["config.yml"])

    # exception
    exception = providers.Factory(ApiException)

    app_config = providers.Factory(AppConfig)
    # Repository
    user_repository = providers.Factory(UserRepository)
    # Service
    user_token_service = providers.Factory(
        UserTokenService, user_repository=user_repository
    )
    auth_service = providers.Factory(AuthService, user_repository=user_repository)
    user_service = providers.Factory(UserService, user_repository=user_repository)

    access_token_factory = providers.Factory(AccessTokenFactory)
    mail_service = providers.Factory(MailService, config=app_config)
    user_register = providers.Factory(
        UserRegisterUseCase,
        user_service=user_service,
        access_token_factory=access_token_factory,
        mail_service=mail_service,
    )
    user_login = providers.Factory(
        UserLoginUseCase,
        auth_service=auth_service,
        exception=exception,
        app_config=app_config,
        access_token_factory=access_token_factory,
    )

    account_creation = providers.Factory(
        AccountCreationUseCase,
        user_repository=user_repository,
        user_token_service=user_token_service,
        exception=exception,
        auth_service=auth_service,
    )
