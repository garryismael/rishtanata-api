
from tortoise import fields, models

from src.constant import DATE_FORMAT, DATE_TIME_FORMAT
from src.domain.auth.model import UserAccount
from src.domain.user.model import User


class UserModelMapper(models.Model):
    id = fields.IntField(pk=True)
    full_name = fields.CharField(max_length=100)
    gender = fields.CharField(max_length=10)
    birthdate = fields.DateField()
    birth_country = fields.CharField(max_length=100, null=True)
    email = fields.CharField(max_length=100, unique=True)
    contact = fields.CharField(max_length=20)
    photo = fields.CharField(max_length=50, null=True)
    verified = fields.BooleanField(max_length=50, default=False)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    def cast(self):
        birthdate = self.birthdate.strftime(DATE_FORMAT)
        created_at = self.created_at.strftime(DATE_TIME_FORMAT)
        updated_at = self.updated_at.strftime(DATE_TIME_FORMAT)

        return User(
            id=self.id,
            full_name=self.full_name,
            gender=self.gender,
            birthdate=birthdate,
            birth_country=self.birth_country,
            email=self.email,
            contact=self.contact,
            photo=self.photo,
            verified=self.verified,
            created_at=created_at,
            updated_at=updated_at,
        )

    class Meta:
        table = "users"

    def __str__(self):
        return self.full_name
