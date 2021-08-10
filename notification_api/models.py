from django.db import models


class Watchlist(models.Model):
    device_id = models.CharField(max_length=200)
    companies = models.ManyToManyField(Company)

    class Meta:
        managed = False


class Company(models.Model):
    company_ticker = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)

    class Meta:
        managed = False
