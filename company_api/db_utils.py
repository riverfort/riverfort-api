from company_api.fmp_api import FMPStockData
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
import pandas as pd
import numpy as np
import logging


def insert_add_on_company(cursor, company_ticker, company_name):
    cursor.execute(
      """
      INSERT INTO company (name, symbol, am_name, am_email, status, isstreak, isaddon)
      VALUES (%s, %s, 'N/A', 'N/A', 'True', False, True)
      """, [company_name, company_ticker])

    cursor.execute("SELECT id FROM company WHERE symbol=%s;", [company_ticker])
    id = cursor.fetchone()[0]

    cursor.execute(
      """
      INSERT INTO fmp_data (id, symbol, name)
      VALUES (%s, %s, %s)
      """, [id, company_ticker, company_name])


def insert_company_profile(cursor, company_ticker):
    fmp_data = FMPStockData()
    profile = fmp_data.get_company_profile(company_ticker)
    normaliser = 0
    if len(profile) > 0 and 'symbol' in profile[0]:
        if profile[0]['exchange'] == "LSE":
            normaliser = 100
        cursor.execute(
          """
          INSERT INTO company_profile (
          company_ticker, company_name, exchange, exchange_type, currency,
          industry, sector, isin, country, normalizer, am_uid)
          VALUES (%s, %s, %s, '', %s, %s, %s, %s, %s, %s, 1)
          """,
          [company_ticker, profile[0]['companyName'], profile[0]['exchange'],
           profile[0]['currency'], profile[0]['industry'], profile[0]['sector'],
           profile[0]['isin'], profile[0]['country'], normaliser])
    else:
        logging.debug_msg("No profile found for company " + company_ticker)


def insert_company_quote(cursor, company_ticker):
    fmp_data = FMPStockData()
    company_quotes = fmp_data.get_company_quote(company_ticker)
    if len(company_quotes) > 0 and 'marketCap' in company_quotes[0]:
        dt_object = datetime.fromtimestamp(company_quotes[0]['timestamp'])
        market_cap = company_quotes[0]['marketCap']
        if market_cap is not None:
            market_cap = round(market_cap, 2)
        price = company_quotes[0]['price']
        if price is not None:
            price = round(price, 2)
        cursor.execute(
          """
          INSERT INTO company_quote (company_ticker, market_cap, price, timestamp)
          VALUES (%s, %s, %s, %s)
          """, [company_ticker, market_cap, price, dt_object])
    else:
        logging.debug_msg("Company quotes for " + company_ticker + " is not present")


def insert_company_trading(cursor, company_ticker):
    fmp_data = FMPStockData()
    start_date = (date.today() + relativedelta(months=-6)).isoformat()
    historical_data = fmp_data.get_historical_data(company_ticker, start_date)
    if 'historical' in historical_data:
        for hd in historical_data['historical']:
            market_date = ''
            open_price = 0
            close = 0
            high = 0
            low = 0
            vwap = 0
            volume = 0
            change_percent = 0

            if 'date' in hd:
                market_date = hd['date']

            if 'open' in hd:
                open_price = round(hd['open'], 2)

            if 'close' in hd:
                close = round(hd['close'], 2)

            if 'high' in hd:
                high = round(hd['high'], 2)

            if 'low' in hd:
                low = round(hd['low'], 2)

            if 'vwap' in hd:
                vwap = round(hd['vwap'], 2)

            if 'volume' in hd:
                volume = round(hd['volume'], 2)

            if 'changePercent' in hd:
                change_percent = round(hd['changePercent'], 2)

            cursor.execute(
              """
              INSERT INTO company_trading
              (company_ticker, market_date, open, close, high, low, vwap, volume, change_percent)
              VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
              """, [company_ticker, market_date, open_price, close, high, low, vwap, volume, change_percent])
    else:
        logging.debug_msg("Historical data for " + company_ticker + " is not present")


def insert_company_adtv(cursor, company_ticker):
    # constant for trading data columns
    VWAP = 6
    VOLUME = 7
    DATE = 1
    NORMALIZER = 9
    EXCHANGE = 10
    CLOSE = 3
    COLUMN_NAMES = ["date", "adtv", "adtv5", "adtv10", "adtv20", "adtv60", "adtv120", "isOutlier", "aadtv", "aadtv5",
                    "aadtv10", "aadtv20", "aadtv60", "aadtv120"]
    cursor.execute(
      """
      SELECT ct.*, cp.normalizer, cp.exchange FROM
      company_trading as ct,
      company_profile as cp WHERE
      ct.company_ticker=cp.company_ticker AND ct.company_ticker=%s
      ORDER BY ct.market_date DESC
      """, [company_ticker])
    trading_data = cursor.fetchall()
    print(trading_data)
    if len(trading_data) <= 0:
        logging.debug_msg("Trading data for company " + company_ticker + " is not present")

    # Create data frame to save adtv, isOutlier & aadtv values
    df = pd.DataFrame(columns=COLUMN_NAMES)
    adtv_list = []
    aadtv_list = []

    # row number of dataframe
    row = 0

    for td in trading_data:
        if td[EXCHANGE] == 'TSE' or td[EXCHANGE] == 'TSX':
            adtv = td[CLOSE] * td[VOLUME]
        else:
            adtv = td[VWAP] * td[VOLUME]

        if td[NORMALIZER] > 0:
            adtv = adtv / td[NORMALIZER]

        adtv_list.append(adtv)
        df.loc[row, 'date'] = td[DATE]
        df.loc[row, 'adtv'] = adtv
        row += 1

    # Create dataframe from adtv_list
    adtv_df = pd.DataFrame(adtv_list)
    size = adtv_df.size

    # Calculate outliers
    quartile_df = adtv_df
    quartile_df.sort_values(0)
    q1, q3 = np.percentile(quartile_df, [25, 75])
    iqr = q3 - q1
    lower_bound = q1 - (1.5 * iqr)
    upper_bound = q3 + (1.5 * iqr)

    for x in range(0, size):
        # Calculate average
        df.loc[x, 'adtv5'] = adtv_df.head(5).mean()[0]
        df.loc[x, 'adtv10'] = adtv_df.head(10).mean()[0]
        df.loc[x, 'adtv20'] = adtv_df.head(20).mean()[0]
        df.loc[x, 'adtv60'] = adtv_df.head(60).mean()[0]
        df.loc[x, 'adtv120'] = adtv_df.head(120).mean()[0]

        adtv_val = adtv_list[x]
        if adtv_val < lower_bound or adtv_val > upper_bound:
            df.loc[x, 'isOutlier'] = True
            df.loc[x, 'aadtv'] = None
            aadtv_list.append(None)
        else:
            df.loc[x, 'isOutlier'] = False
            df.loc[x, 'aadtv'] = adtv_val
            aadtv_list.append(adtv_val)

        adtv_df = adtv_df.drop(x)

    # Create dataframe from aadtv_list
    aadtv_df = pd.DataFrame(aadtv_list)
    size = aadtv_df.size
    for x in range(0, size):
        # Calculate average
        df.loc[x, 'aadtv5'] = aadtv_df.head(5).mean()[0]
        df.loc[x, 'aadtv10'] = aadtv_df.head(10).mean()[0]
        df.loc[x, 'aadtv20'] = aadtv_df.head(20).mean()[0]
        df.loc[x, 'aadtv60'] = aadtv_df.head(60).mean()[0]
        df.loc[x, 'aadtv120'] = aadtv_df.head(120).mean()[0]

        aadtv_df = aadtv_df.drop(x)

    # Save all values in company_adtv table
    for val in range(0, len(trading_data)):

        aadtv = df.at[val, 'aadtv']
        if df.at[val, 'isOutlier'] is False:
            aadtv = round(aadtv, 2)

        cursor.execute(
          """
          INSERT INTO
          company_adtv
          (company_ticker, date, adtv, adtv5, adtv10, adtv20, adtv60, adtv120,
          isoutlier, aadtv, aadtv5, aadtv10, aadtv20, aadtv60, aadtv120)
          VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
          """,
          [company_ticker, df.at[val, 'date'],
           round(df.at[val, 'adtv'], 2), round(df.at[val, 'adtv5'], 2), round(df.at[val, 'adtv10'], 2),
           round(df.at[val, 'adtv20'], 2), round(df.at[val, 'adtv60'], 2), round(df.at[val, 'adtv120'], 2),
           df.at[val, 'isOutlier'], aadtv, round(df.at[val, 'aadtv5'], 2), round(df.at[val, 'aadtv10'], 2),
           round(df.at[val, 'aadtv20'], 2), round(df.at[val, 'aadtv60'], 2), round(df.at[val, 'aadtv120'], 2)])
