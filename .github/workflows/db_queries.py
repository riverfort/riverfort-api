# ACCOUNT_MANAGER
account_manager_table_query = "CREATE TABLE IF NOT EXISTS account_manager (am_uid SERIAL PRIMARY KEY, " \
                              "am_name VARCHAR(100), " \
                              "am_email VARCHAR(100), " \
                              "am_mobile VARCHAR(20))"

account_manager_insert_query = "INSERT INTO account_manager(am_name, am_email, am_mobile) " \
                               "VALUES(%s, %s, %s) RETURNING am_uid"

account_manager_select_query = """SELECT am_uid FROM account_manager WHERE account_manager.am_name = %s"""

# COMPANY_PROFILE
# Create table company_profile
company_profile_table_query = "CREATE TABLE IF NOT EXISTS company_profile (company_ticker VARCHAR(25) PRIMARY KEY, " \
                              "company_name VARCHAR(100) NOT NULL, " \
                              "exchange VARCHAR(100) NOT NULL, " \
                              "exchange_type VARCHAR(25)," \
                              "currency VARCHAR(5)," \
                              "industry VARCHAR(100), " \
                              "sector VARCHAR(100), " \
                              "isin VARCHAR(50), " \
                              "country VARCHAR(50), " \
                              "normalizer INTEGER," \
                              "am_uid INTEGER REFERENCES account_manager(am_uid)," \
                              "created_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP)"

company_profile_insert_query = "INSERT INTO company_profile(company_ticker, company_name, exchange, exchange_type, " \
                               "currency, industry, sector, isin, country, normalizer, am_uid) VALUES(%s, %s, %s, " \
                               "%s, %s, %s, %s, %s, %s, %s, %s) RETURNING company_ticker"

company_profile_select_query = "SELECT company_ticker FROM company_profile"
cp_tickers_select_query = "SELECT company_ticker FROM company_profile WHERE exchange NOT IN " \
                          "('TSX', 'TSE')"
cp_tsx_tickers_select_query = "SELECT company_ticker FROM company_profile WHERE exchange IN ('TSX', 'TSE')"

# COMPANY_EXCHANGE
company_quote_table_query = "CREATE TABLE IF NOT EXISTS company_quote (company_ticker VARCHAR(10) REFERENCES " \
                            "company_profile(company_ticker) PRIMARY KEY, " \
                            "market_cap DOUBLE PRECISION, " \
                            "price DOUBLE PRECISION," \
                            "timestamp TIMESTAMP NOT NULL)"

# insert query
company_quote_insert_query = "INSERT INTO company_quote(company_ticker, market_cap, price, timestamp) " \
                             "VALUES(%s, %s, %s, %s) RETURNING company_ticker"

company_quote_select_query = "SELECT timestamp FROM company_quote WHERE company_ticker = %s"

company_quote_update_query = "UPDATE company_quote SET market_cap = %s, price = %s, timestamp = %s WHERE " \
                             "company_ticker = %s"

# COMPANY_TRADING
company_trading_table_query = "CREATE TABLE IF NOT EXISTS company_trading (company_ticker VARCHAR(10) REFERENCES " \
                              "company_profile(company_ticker), " \
                              "market_date DATE NOT NULL, " \
                              "open DOUBLE PRECISION, " \
                              "close DOUBLE PRECISION," \
                              "high DOUBLE PRECISION, " \
                              "low DOUBLE PRECISION, " \
                              "vwap DOUBLE PRECISION," \
                              "volume DOUBLE PRECISION," \
                              "change_percent DOUBLE PRECISION," \
                              "PRIMARY KEY(company_ticker, market_date))"

company_trading_insert_query = "INSERT INTO company_trading(company_ticker, market_date, open, close, high, low, " \
                               "vwap, volume, change_percent) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s) " \
                               "RETURNING company_ticker"

company_trading_select_query = "SELECT ct.*, cp.normalizer, cp.exchange FROM company_trading as ct, " \
                               "company_profile as cp WHERE ct.company_ticker=cp.company_ticker and " \
                               "ct.company_ticker = %s ORDER BY ct.market_date DESC"

select_max_date = "select max(market_date) from company_trading where company_ticker = %s"

# COMPANY_adtv
company_adtv_table_query = "CREATE TABLE IF NOT EXISTS company_adtv (company_ticker VARCHAR(10), " \
                           "date DATE NOT NULL, " \
                           "adtv DOUBLE PRECISION, " \
                           "adtv5 DOUBLE PRECISION, " \
                           "adtv10 DOUBLE PRECISION," \
                           "adtv20 DOUBLE PRECISION," \
                           "adtv60 DOUBLE PRECISION, " \
                           "adtv120 DOUBLE PRECISION, " \
                           "isOutlier boolean," \
                           "aadtv DOUBLE PRECISION, " \
                           "aadtv5 DOUBLE PRECISION, " \
                           "aadtv10 DOUBLE PRECISION," \
                           "aadtv20 DOUBLE PRECISION," \
                           "aadtv60 DOUBLE PRECISION, " \
                           "aadtv120 DOUBLE PRECISION, " \
                           "PRIMARY KEY(company_ticker, date))"

company_adtv_insert_query = "INSERT INTO company_adtv(company_ticker, date, adtv, adtv5, adtv10, adtv20, adtv60, " \
                            "adtv120, isOutlier, aadtv, aadtv5, aadtv10, aadtv20, aadtv60, aadtv120) VALUES(%s, %s, " \
                            "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING company_ticker"

company_adtv_delete_query = "DELETE FROM company_adtv"

# COMPANY_ACCOUNT_MANAGER
# Create table company_account_manager
# print("Creating table company_account_manager....")
# company_account_manager_table_query = f"CREATE TABLE IF NOT EXISTS company_account_manager (" \
#                                       f"company_ticker VARCHAR(10) PRIMARY KEY, " \
#                                       f"am_uid VARCHAR(100))"
# db.create_table(company_account_manager_table_query)

# COMPANY
company_table_query = "CREATE TABLE IF NOT EXISTS company (id SERIAL PRIMARY KEY," \
                      "name VARCHAR(100)," \
                      "symbol VARCHAR(50), " \
                      "am_name VARCHAR(100), " \
                      "am_email VARCHAR(100), " \
                      "region VARCHAR(100)," \
                      "status varchar(5)," \
                      "isStreak BOOLEAN," \
                      "isAddon BOOLEAN)"

# insert query
company_insert_query = "INSERT INTO company(name, symbol, am_name, am_email, region, status, isStreak, isAddon) " \
                       "VALUES(%s, %s, %s, %s, %s, %s, %s, %s) RETURNING id"
# select query
company_select_query = """SELECT symbol FROM company"""
select_failed_records = """SELECT * FROM company WHERE status = 'False' and symbol NOT IN
                        ('DELISTED', 'PRIVATE', '', '#N/A', 'CLOSED')"""

# Update query
update_status = "UPDATE company SET status = %s WHERE symbol = %s"

# All companies
companies_list = "CREATE TABLE IF NOT EXISTS companies (id SERIAL NOT NULL," \
                 "name VARCHAR(100)," \
                 "symbol VARCHAR(50), " \
                 "exchange varchar(25)," \
                 "industry VARCHAR(50), sector VARCHAR(50)," \
                 "currency VARCHAR(5), isin VARCHAR(50))"

companies_list_insert_query = "INSERT INTO companies(name, symbol, exchange, industry, sector, currency, isin) " \
                              "VALUES(%s, %s, %s, %s, %s, %s, %s) RETURNING id"

companies_select_query = "SELECT symbol FROM companies"

# fmp_data
fmp_data_table_query = "CREATE TABLE IF NOT EXISTS fmp_data (id INTEGER REFERENCES company(id), " \
                       "symbol VARCHAR(40), name VARCHAR(100), currency VARCHAR(25), exchange VARCHAR(50), " \
                       "short_exchange VARCHAR(25))"

fmp_data_insert_query = "INSERT INTO fmp_data(id, symbol, name, currency, exchange, short_exchange)" \
                        "VALUES(%s, %s, %s, %s, %s, %s) RETURNING id"

fmp_data_select_query = "SELECT s.symbol, s.am_name, s.am_email, f.symbol, f.name, f.currency, f.exchange, " \
                        "f.short_exchange FROM company as s, fmp_data as f where s.id = f.id and " \
                        "f.symbol not in (select company_ticker from company_profile)"

# iex_data
iex_data_table_query = "CREATE TABLE IF NOT EXISTS iex_data (id INTEGER REFERENCES company(id)," \
                       "symbol VARCHAR(50), " \
                       "cik VARCHAR(50)," \
                       "exchange varchar(25)," \
                       "securityName VARCHAR(100), " \
                       "securityType VARCHAR(5), " \
                       "region VARCHAR(50)," \
                       "sector VARCHAR(150))"

iex_data_insert_query = "INSERT INTO iex_data(id, symbol,cik, exchange, securityName, securityType, region, sector) " \
                        "VALUES(%s, %s, %s, %s, %s, %s, %s, %s) RETURNING id"

iex_data_select_query = "SELECT s.symbol, s.am_name, s.am_email, i.* FROM company as s, iex_data as i " \
                        "where s.id = i.id and i.symbol not in (select company_ticker from company_profile)"
