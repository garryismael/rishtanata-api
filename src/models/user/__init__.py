from tortoise import fields, models

from src.constant import DATE_FORMAT
from src.domain.user.model import User


class UserModelMapper(models.Model):
    id = fields.IntField(pk=True)
    full_name = fields.CharField(max_length=100)
    birthdate = fields.DateField()
    birth_city = fields.CharField(max_length=100, null=True)
    birth_country = fields.CharField(max_length=100, null=True)
    gender = fields.CharField(max_length=10)
    address = fields.CharField(max_length=50, null=True)
    email = fields.CharField(max_length=100, unique=True)
    cell_phone = fields.CharField(max_length=20)
    home_phone = fields.CharField(max_length=20, null=True)
    photo = fields.CharField(max_length=50, null=True)
    nationality = fields.CharField(max_length=50, null=True)
    ethnic_group = fields.CharField(max_length=50, null=True)
    marital_status = fields.CharField(max_length=50, null=True)
    height = fields.IntField(null=True)
    weight = fields.IntField(null=True)
    complexion = fields.IntField(null=True)
    occupation = fields.CharField(max_length=50, null=True)
    verified = fields.BooleanField(default=False)
    profile_active = fields.BooleanField(default=False)
    password = fields.CharField(max_length=150, null=True)
    is_admin = fields.BooleanField(default=False)

    def cast(self):
        birthdate = self.birthdate.strftime(DATE_FORMAT)

        return User(
            id=self.id,
            full_name=self.full_name,
            birthdate=birthdate,
            birth_city=self.birth_city,
            birth_country=self.birth_country,
            gender=self.gender,
            address=self.address,
            email=self.email,
            cell_phone=self.cell_phone,
            home_phone=self.home_phone,
            photo=self.photo,
            nationality=self.nationality,
            ethnic_group=self.ethnic_group,
            marital_status=self.marital_status,
            height=self.height,
            weight=self.weight,
            complexion=self.complexion,
            occupation=self.occupation,
            verified=self.verified,
            profile_active=self.profile_active,
            password=self.password,
            is_admin=self.is_admin,
        )

    class Meta:
        table = "users"

    def __str__(self):
        return self.full_name
