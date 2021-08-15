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


class CompanyNews(models.Model):
    company_ticker = models.OneToOneField(Company, models.DO_NOTHING, db_column='company_ticker', primary_key=True)
    pub_date = models.DateTimeField()
    title = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'company_news'
        unique_together = (('company_ticker', 'pub_date'),)


class UserDevice(models.Model):
    device_token = models.CharField(primary_key=True, max_length=200)

    class Meta:
        managed = False
        db_table = 'user_device'


class Watchlist(models.Model):
    watchlist_id = models.AutoField(primary_key=True)
    device_token = models.ForeignKey(UserDevice, models.DO_NOTHING, db_column='device_token')
    company_ticker = models.ForeignKey(Company, models.DO_NOTHING, db_column='company_ticker')

    class Meta:
        managed = False
        db_table = 'watchlist'
        unique_together = (('device_token', 'company_ticker'),)
