import requests
import logging


class FMPStockData:
    def __init__(self):
        self.apiKey = "2797db3c7193bf4ec7231be3cba5f27c"

    def search_symbol(self, company_name):
        try:
            params = {
                'query': company_name,
                'apikey': self.apiKey
            }
            response = requests.get('https://financialmodelingprep.com/api/v3/search', params)
            search_result = []
            if response.status_code == 200:
                search_result = response.json()
            else:
                logging.error("Unable to search :" + company_name, response.reason)

            return search_result
        except requests.exceptions:
            logging.debug_msg("Exception in search_symbol")

    def search_using_ticker(self, ticker):
        try:
            params = {
                'query': ticker,
                'apikey': self.apiKey
            }
            response = requests.get('https://financialmodelingprep.com/api/v3/search-ticker', params)
            search_result = []
            if response.status_code == 200:
                search_result = response.json()
            else:
                logging.error("Unable to search :" + ticker, response.reason)

            return search_result
        except requests.exceptions:
            logging.debug_msg("Exception in search_symbol")

    def get_company_profile(self, symbol):
        try:
            params = {
                'apikey': self.apiKey
            }
            response = requests.get('https://financialmodelingprep.com/api/v3/profile/' + symbol, params)
            profile_data = []
            if response.status_code == 200:
                profile_data = response.json()
            else:
                logging.error('Unable to find profile for company: ' + symbol, response.reason)

            return profile_data
        except requests.exceptions:
            logging.debug_msg("Exception in get_company_profile")

    def get_company_quote(self, company_ticker):
        try:
            params = {
                'apikey': self.apiKey
            }
            response = requests.get('https://financialmodelingprep.com/api/v3/quote/' + company_ticker, params)
            data = []
            if response.status_code == 200:
                data = response.json()
            else:
                logging.error("Unable to load company quotes: ", response.reason)

            return data
        except requests.exceptions:
            logging.debug_msg("Exception in get_company_quote")

    def get_historical_data(self, company_ticker, start_date):
        try:
            params = {
                'apikey': self.apiKey,
                'from': start_date
            }

            response = requests.get('https://financialmodelingprep.com/api/v3/historical-price-full/' + company_ticker,
                                    params)
            data = []
            if response.status_code == 200:
                data = response.json()
            else:
                logging.error("Unable to load company historic data: ", response.reason)

            return data
        except requests.exceptions:
            logging.debug_msg("Exception in get_historical_data")

    def get_all_companies(self, exchange):
        try:
            params = {
                'apikey': self.apiKey,
                'exchange': exchange,
                'limit': 10000,
                'query': ''
            }
            response = requests.get('https://financialmodelingprep.com/api/v3/search', params)
            data = []
            if response.status_code == 200:
                data = response.json()
            else:
                logging.error("Unable to load data: ", response.reason)

            return data

        except requests.exceptions:
            logging.debug_msg("Exception in get_all_companies")
