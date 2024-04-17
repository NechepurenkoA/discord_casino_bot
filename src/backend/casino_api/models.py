from django.db import models

from discord_users.models import DiscordUser


class Stats(models.Model):
    discord_user = models.OneToOneField(
        DiscordUser, on_delete=models.SET_NULL, related_name="stats"
    )
    wins = models.IntegerField(verbose_name="wins", default=0, blank=False, null=False)
    losses = models.IntegerField(
        verbose_name="losses", default=0, blank=False, null=False
    )
    earned = models.BigIntegerField(
        verbose_name="money_earned", default=0, blank=False, null=False
    )
    lost = models.BigIntegerField(
        verbose_name="money_lost", default=0, blank=False, null=False
    )
