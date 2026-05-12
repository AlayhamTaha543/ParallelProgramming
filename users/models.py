from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    class Roles(models.TextChoices):
        CUSTOMER= 'CUSTOMER', 'Customer'
        STORE_OWNER = 'STORE_OWNER', 'Store Owner'

    role = models.CharField(
        max_length=20,
        choices=Roles.choices
    )

