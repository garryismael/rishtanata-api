from tortoise import fields, models
from src.constant import DATE_TIME_FORMAT

from src.domain.account.model import Account, AccountResponseDTO
from src.models.user import UserModelMapper


class AccountModelMapper(models.Model):
    id = fields.IntField(pk=True)
    user: UserModelMapper = fields.OneToOneField(
        "models.UserModelMapper", related_name="account", null=False
    )
    password = fields.CharField(max_length=150)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "accounts"

    def cast(self) -> AccountResponseDTO:
        created_at = self.created_at.strftime(DATE_TIME_FORMAT)
        updated_at = self.updated_at.strftime(DATE_TIME_FORMAT)

        return AccountResponseDTO(
            id=self.id,
            user=self.user.cast(),
            created_at=created_at,
            updated_at=updated_at,
        )

    @property
    def account(self):
        created_at = self.created_at.strftime(DATE_TIME_FORMAT)
        updated_at = self.updated_at.strftime(DATE_TIME_FORMAT)
        return Account(
            id=self.id,
            user=self.user.cast(),
            password=self.password,
            created_at=created_at,
            updated_at=updated_at,
        )

    def __str__(self):
        return self.email
