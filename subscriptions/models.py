from django.db import models


class Subscription(models.Model):
    ticker = models.CharField(max_length=10)
    email = models.EmailField()
    min_price = models.FloatField(blank=True, null=True)
    max_price = models.FloatField(blank=True, null=True)
