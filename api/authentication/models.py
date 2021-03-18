from django.contrib.auth.models import AbstractUser

from api.main.models import BaseModel


class User(BaseModel, AbstractUser):
    pass

    class Meta:
        db_table = 'user'
