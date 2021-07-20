from Configuration.config import DatabaseConnection
import db_queries as query

# Create class Objects
db = DatabaseConnection("testing_database", "user", "password", "localhost", 5432)

# create all tables
# db.create_table(companies_list)
print("Creating table company")
db.create_table(query.company_table_query)

print("Create table fmp_data")
db.create_table(query.fmp_data_table_query)

print("Create table iex_data")
db.create_table(query.iex_data_table_query)

print("Creating table account_manager")
db.create_table(query.account_manager_table_query)
db.insert_data(query.account_manager_insert_query, ('N/A', 'N/A', 'N/A'))

print("Creating table company_profile")
db.create_table(query.company_profile_table_query)

print("Creating table company_quote")
db.create_table(query.company_quote_table_query)

print("Creating table company_trading")
db.create_table(query.company_trading_table_query)

print("Creating table company_adtv")
db.create_table(query.company_adtv_table_query)
