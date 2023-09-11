from core.configuration.config import Config
import requests

class GetApi:
# Access Financial Modeling Prep APIs
# It constructs the query string depending on the API and fetches the data
# The data will be retured from the API is in the JSON format
# The class is the base class for all the APIs. It does all the functionality of building the URL
# and fetches the data.
# All the sub classes just needs to provide the query string depending on the API. 
# 
    config = Config()
    def __init__(self, query_string) -> None:
        self.api_config = GetApi.config.load_config()['FmpApi']
        self.api_response = None
        self.query_string = query_string
    
    def get_uri(self):
        return self.api_config['uri']
    
    def get_api_key(self):
        return self.api_config['key']
    
    def get_url(self):
        return self.get_uri() + self.query_string + self.get_api_key()
    
    def fetch(self):
        url = self.get_url()
        response = requests.get(url)
        jsondata = response.json()
        return jsondata



class SP500(GetApi):
# The class just need to fill in the details of the query string for SP500. The Base class 
# takes care of all the execution of the rest of the functionality

    def __init__(self)-> None:
        super().__init__("sp500_constituent?")

class Nasdaq(GetApi):
# The class just need to fill in the details of the query string for NASDAQ. The Base class
# takes care of all the execution of the rest of the functionality

    def __init__(self)->None :
        super().__init__("nasdaq_constituent?")

class Dowjones(GetApi):
# The class just need to fill in the details of the query string for DOWJONES. The Base class
# takes care of all the execution of the rest of the functionality
    def __init__(self)->None :
        super().__init__("dowjones_constituent?")

class Stockprices(GetApi):
    def __init__(self)->None :
        super().__init__("quote/AAPL?")

    
class Historicprices(GetApi):
    def __init__(self)->None :
        super().__init__("historical-price-full/AAPL?from=2017-01-01&to=2023-09-07&")
    # def __init__(self, symbol, start_date, end_date) -> None:
    #     query_string = f"historical-price-full/{symbol}?from={start_date}&to={end_date}&"
    #     super().__init__(query_string)

    # def fetch_historical_prices_for_symbols(symbols, start_date, end_date):
    #     historical_prices = {}
    #     for symbol in symbols:
    #         api = HistoricalPrices(symbol, start_date, end_date)
    #         data = api.fetch()
    #         historical_prices[symbol] = data
    #     return historical_prices

class Historic_market_cap(GetApi):
    def __init__(self)->None:
        super().__init__("historical-market-capitalization/AAPL?limit=2000&")


class Global_stocks(GetApi):
    def __init__(self)->None:
        super().__init__("stock/list?")

class Global_etfs(GetApi):
    def __init__(self)->None:
        super().__init__("etf/list?")