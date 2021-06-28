# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccountManager(models.Model):
    am_uid = models.AutoField(primary_key=True)
    am_name = models.CharField(max_length=100, blank=True, null=True)
    am_email = models.CharField(max_length=100, blank=True, null=True)
    am_mobile = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_manager'


class CompanyAdtv(models.Model):
    company_ticker = models.CharField(primary_key=True, max_length=10)
    date = models.DateField()
    adtv = models.FloatField(blank=True, null=True)
    adtv5 = models.FloatField(blank=True, null=True)
    adtv10 = models.FloatField(blank=True, null=True)
    adtv20 = models.FloatField(blank=True, null=True)
    adtv60 = models.FloatField(blank=True, null=True)
    adtv120 = models.FloatField(blank=True, null=True)
    isoutlier = models.BooleanField(blank=True, null=True)
    aadtv = models.FloatField(blank=True, null=True)
    aadtv5 = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    aadtv10 = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    aadtv20 = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    aadtv60 = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    aadtv120 = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company_adtv'
        unique_together = (('company_ticker', 'date'),)


class CompanyProfile(models.Model):
    company_ticker = models.CharField(primary_key=True, max_length=25)
    company_name = models.CharField(max_length=100)
    exchange = models.CharField(max_length=100)
    exchange_type = models.CharField(max_length=25, blank=True, null=True)
    currency = models.CharField(max_length=5, blank=True, null=True)
    industry = models.CharField(max_length=100, blank=True, null=True)
    sector = models.CharField(max_length=100, blank=True, null=True)
    isin = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    normalizer = models.IntegerField(blank=True, null=True)
    am_uid = models.ForeignKey(AccountManager, models.DO_NOTHING, db_column='am_uid', blank=True, null=True)
    created_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'company_profile'


class CompanyQuote(models.Model):
    company_ticker = models.OneToOneField(
      CompanyProfile, models.DO_NOTHING, db_column='company_ticker', primary_key=True)
    market_cap = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'company_quote'


class CompanyTrading(models.Model):
    company_ticker = models.OneToOneField(
      CompanyProfile, models.DO_NOTHING, db_column='company_ticker', primary_key=True)
    market_date = models.DateField()
    open = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    vwap = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)
    change_percent = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company_trading'
        unique_together = (('company_ticker', 'market_date'),)


class FmpData(models.Model):
    id = models.OneToOneField('StreakCompanies', models.DO_NOTHING, db_column='id', blank=True, primary_key=True)
    symbol = models.CharField(max_length=40, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    currency = models.CharField(max_length=25, blank=True, null=True)
    exchange = models.CharField(max_length=50, blank=True, null=True)
    short_exchange = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fmp_data'


class IexData(models.Model):
    id = models.OneToOneField('StreakCompanies', models.DO_NOTHING, db_column='id', blank=True, primary_key=True)
    symbol = models.CharField(max_length=50, blank=True, null=True)
    cik = models.CharField(max_length=50, blank=True, null=True)
    exchange = models.CharField(max_length=25, blank=True, null=True)
    securityname = models.CharField(max_length=100, blank=True, null=True)
    securitytype = models.CharField(max_length=5, blank=True, null=True)
    region = models.CharField(max_length=50, blank=True, null=True)
    sector = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'iex_data'


class StreakCompanies(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    symbol = models.CharField(max_length=50, blank=True, null=True)
    am_name = models.CharField(max_length=100, blank=True, null=True)
    am_email = models.CharField(max_length=100, blank=True, null=True)
    region = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'streak_companies'
