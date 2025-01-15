from django.contrib.auth.models import AbstractUser
from django.db import models

class UserModel(AbstractUser):
    class Roles(models.TextChoices):
        ORDINARY = 'ORDINARY', 'Ordinary'
        MANAGER = 'MANAGER', 'Manager'
        CASHIER = 'CASHIER', 'Cashier'

    role = models.CharField(
        max_length=20,
        choices=Roles.choices,
        default=Roles.ORDINARY,
    )

