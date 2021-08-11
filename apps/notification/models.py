# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Company(models.Model):
    company_ticker = models.CharField(primary_key=True, max_length=25)
    company_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'company'


class UserDevice(models.Model):
    device_id = models.CharField(primary_key=True, max_length=200)

    class Meta:
        managed = False
        db_table = 'user_device'


class Watchlist(models.Model):
    device = models.OneToOneField(UserDevice, models.DO_NOTHING, primary_key=True)
    company_ticker = models.ForeignKey(Company, models.DO_NOTHING, db_column='company_ticker')

    class Meta:
        managed = False
        db_table = 'watchlist'
        unique_together = (('device', 'company_ticker'),)