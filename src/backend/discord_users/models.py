from django.contrib.auth.models import AbstractBaseUser
from django.db import models


class DiscordUser(AbstractBaseUser):
    discord_id = models.CharField(
        verbose_name="discord_id",
        max_length=18,
        unique=True,
        blank=False,
        null=False,
    )
    balance = models.BigIntegerField(
        verbose_name="user_balance",
        default=2000,
    )
