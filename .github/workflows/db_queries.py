# ACCOUNT_MANAGER
account_manager_table_query = f"CREATE TABLE IF NOT EXISTS account_manager (am_uid SERIAL PRIMARY KEY, " \
                              f"am_name VARCHAR(100), " \
                              f"am_email VARCHAR(100), " \
                              f"am_mobile VARCHAR(20))"

account_manager_insert_query = f"INSERT INTO account_manager(am_name, am_email, am_mobile) " \
                               f"VALUES(%s, %s, %s) RETURNING am_uid"

account_manager_select_query = """SELECT am_uid FROM account_manager WHERE account_manager.am_name = %s"""

# COMPANY_PROFILE
# Create table company_profile
company_profile_table_query = f"CREATE TABLE IF NOT EXISTS company_profile (company_ticker VARCHAR(25) PRIMARY KEY, " \
                              f"company_name VARCHAR(100) NOT NULL, " \
                              f"exchange VARCHAR(100) NOT NULL, " \
                              f"exchange_type VARCHAR(25)," \
                              f"currency VARCHAR(5)," \
                              f"industry VARCHAR(100), " \
                              f"sector VARCHAR(100), " \
                              f"isin VARCHAR(50), " \
                              f"country VARCHAR(50), " \
                              f"normalizer INTEGER," \
                              f"am_uid INTEGER REFERENCES account_manager(am_uid)," \
                              f"created_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP)"

company_profile_insert_query = f"INSERT INTO company_profile(company_ticker, company_name, exchange, exchange_type, " \
                               f"currency, industry, sector, isin, country, normalizer, am_uid) VALUES(%s, %s, %s, " \
                               f"%s, %s, %s, %s, %s, %s, %s, %s) RETURNING company_ticker"

company_profile_select_query = f"SELECT company_ticker FROM company_profile"
cp_tickers_select_query = f"SELECT company_ticker FROM company_profile WHERE exchange NOT IN " \
                          f"('TSX', 'TSE')"
cp_tsx_tickers_select_query = f"SELECT company_ticker FROM company_profile WHERE exchange IN ('TSX', 'TSE')"

# COMPANY_EXCHANGE
company_quote_table_query = f"CREATE TABLE IF NOT EXISTS company_quote (company_ticker VARCHAR(10) REFERENCES " \
                            f"company_profile(company_ticker) PRIMARY KEY, " \
                            f"market_cap DOUBLE PRECISION, " \
                            f"price DOUBLE PRECISION," \
                            f"timestamp TIMESTAMP NOT NULL)"

# insert query
company_quote_insert_query = f"INSERT INTO company_quote(company_ticker, market_cap, price, timestamp) " \
                             f"VALUES(%s, %s, %s, %s) RETURNING company_ticker"

company_quote_select_query = f"SELECT timestamp FROM company_quote WHERE company_ticker = %s"

company_quote_update_query = f"UPDATE company_quote SET market_cap = %s, price = %s, timestamp = %s WHERE " \
                             f"company_ticker = %s"

# COMPANY_TRADING
company_trading_table_query = f"CREATE TABLE IF NOT EXISTS company_trading (company_ticker VARCHAR(10) REFERENCES " \
                              f"company_profile(company_ticker), " \
                              f"market_date DATE NOT NULL, " \
                              f"open DOUBLE PRECISION, " \
                              f"close DOUBLE PRECISION," \
                              f"high DOUBLE PRECISION, " \
                              f"low DOUBLE PRECISION, " \
                              f"vwap DOUBLE PRECISION," \
                              f"volume DOUBLE PRECISION," \
                              f"change_percent DOUBLE PRECISION," \
                              f"PRIMARY KEY(company_ticker, market_date))"

company_trading_insert_query = f"INSERT INTO company_trading(company_ticker, market_date, open, close, high, low, " \
                               f"vwap, volume, change_percent) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s) " \
                               f"RETURNING company_ticker"

company_trading_select_query = f"SELECT ct.*, cp.normalizer, cp.exchange FROM company_trading as ct, " \
                               f"company_profile as cp WHERE ct.company_ticker=cp.company_ticker and " \
                               f"ct.company_ticker = %s ORDER BY ct.market_date DESC"

select_max_date = f"select max(market_date) from company_trading where company_ticker = %s"

# COMPANY_adtv
company_adtv_table_query = f"CREATE TABLE IF NOT EXISTS company_adtv (company_ticker VARCHAR(10), " \
                           f"date DATE NOT NULL, " \
                           f"adtv DOUBLE PRECISION, " \
                           f"adtv5 DOUBLE PRECISION, " \
                           f"adtv10 DOUBLE PRECISION," \
                           f"adtv20 DOUBLE PRECISION," \
                           f"adtv60 DOUBLE PRECISION, " \
                           f"adtv120 DOUBLE PRECISION, " \
                           f"isOutlier boolean," \
                           f"aadtv DOUBLE PRECISION, " \
                           f"aadtv5 DOUBLE PRECISION, " \
                           f"aadtv10 DOUBLE PRECISION," \
                           f"aadtv20 DOUBLE PRECISION," \
                           f"aadtv60 DOUBLE PRECISION, " \
                           f"aadtv120 DOUBLE PRECISION, " \
                           f"PRIMARY KEY(company_ticker, date))"

company_adtv_insert_query = f"INSERT INTO company_adtv(company_ticker, date, adtv, adtv5, adtv10, adtv20, adtv60, " \
                            f"adtv120, isOutlier, aadtv, aadtv5, aadtv10, aadtv20, aadtv60, aadtv120) VALUES(%s, %s, " \
                            f"%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING company_ticker"

company_adtv_delete_query = f"DELETE FROM company_adtv"

# COMPANY_ACCOUNT_MANAGER
# Create table company_account_manager
# print("Creating table company_account_manager....")
# company_account_manager_table_query = f"CREATE TABLE IF NOT EXISTS company_account_manager (" \
#                                       f"company_ticker VARCHAR(10) PRIMARY KEY, " \
#                                       f"am_uid VARCHAR(100))"
# db.create_table(company_account_manager_table_query)

# COMPANY
company_table_query = f"CREATE TABLE IF NOT EXISTS company (id SERIAL PRIMARY KEY," \
                      f"name VARCHAR(100)," \
                      f"symbol VARCHAR(50), " \
                      f"am_name VARCHAR(100), " \
                      f"am_email VARCHAR(100), " \
                      f"region VARCHAR(100)," \
                      f"status varchar(5)," \
                      f"isStreak BOOLEAN," \
                      f"isAddon BOOLEAN)"

# insert query
company_insert_query = f"INSERT INTO company(name, symbol, am_name, am_email, region, status, isStreak, isAddon) " \
                       f"VALUES(%s, %s, %s, %s, %s, %s, %s, %s) RETURNING id"
# select query
company_select_query = """SELECT symbol FROM company"""
select_failed_records = """SELECT * FROM company WHERE status = 'False' and symbol NOT IN 
                        ('DELISTED', 'PRIVATE', '', '#N/A', 'CLOSED')"""

# Update query
update_status = f"UPDATE company SET status = %s WHERE symbol = %s"

# All companies
companies_list = f"CREATE TABLE IF NOT EXISTS companies (id SERIAL NOT NULL," \
                 f"name VARCHAR(100)," \
                 f"symbol VARCHAR(50), " \
                 f"exchange varchar(25)," \
                 f"industry VARCHAR(50), sector VARCHAR(50)," \
                 f"currency VARCHAR(5), isin VARCHAR(50))"

companies_list_insert_query = f"INSERT INTO companies(name, symbol, exchange, industry, sector, currency, isin) " \
                              f"VALUES(%s, %s, %s, %s, %s, %s, %s) RETURNING id"

companies_select_query = f"SELECT symbol FROM companies"

# fmp_data
fmp_data_table_query = f"CREATE TABLE IF NOT EXISTS fmp_data (id INTEGER REFERENCES company(id), " \
                       f"symbol VARCHAR(40), name VARCHAR(100), currency VARCHAR(25), exchange VARCHAR(50), " \
                       f"short_exchange VARCHAR(25))"

fmp_data_insert_query = f"INSERT INTO fmp_data(id, symbol, name, currency, exchange, short_exchange) VALUES(%s, %s, %s, " \
                        f"%s, %s, %s) RETURNING id"

fmp_data_select_query = f"SELECT s.symbol, s.am_name, s.am_email, f.symbol, f.name, f.currency, f.exchange, " \
                        f"f.short_exchange FROM company as s, fmp_data as f where s.id = f.id and " \
                        f"f.symbol not in (select company_ticker from company_profile)"

# iex_data
iex_data_table_query = f"CREATE TABLE IF NOT EXISTS iex_data (id INTEGER REFERENCES company(id)," \
                       f"symbol VARCHAR(50), " \
                       f"cik VARCHAR(50)," \
                       f"exchange varchar(25)," \
                       f"securityName VARCHAR(100), " \
                       f"securityType VARCHAR(5), " \
                       f"region VARCHAR(50)," \
                       f"sector VARCHAR(150))"

iex_data_insert_query = f"INSERT INTO iex_data(id, symbol,cik, exchange, securityName, securityType, region, sector) " \
                        f"VALUES(%s, %s, %s, %s, %s, %s, %s, %s) RETURNING id"

iex_data_select_query = f"SELECT s.symbol, s.am_name, s.am_email, i.* FROM company as s, iex_data as i " \
                        f"where s.id = i.id and i.symbol not in (select company_ticker from company_profile)"
