"""
The purpose of this stock_prices_api.py file is to provide the query_strings of the Global stocks, historical data and daily prices to the GetApi class in the get_api.py module.

This module imports the GetApi class from pulse.fmpapi.get_api

"""

from pulse.fmpapi.get_api import GetApi
from core.configuration.config_singleton import config_singleton_a
import datetime

class Global_stocks(GetApi):
    """
    This class just needs to fill in the details of the query string for global stocks. The Base class 
    takes care of all the execution of the rest of the functionality.

    we are passing the GetApi class object as a parameter for this class. 

    constructor is defined by using the __init__() fucntion to pass the query_string "stock/list?".
    """

    def __init__(self)->None:

        super().__init__("stock/list?")


class Historical_prices(GetApi):
    """
    This class just needs to fill in the details of the query string for Historical prices between certain dates. The Base class 
    takes care of all the execution of the rest of the functionality.

    we are passing the GetApi class object as a parameter for this class. 

    constructor is defined by using the __init__() fucntion to pass the query_string.

    Here, query_string contains the symbol of the company, from and to dates (check the API documentation and source code for more details). 
    """

    def __init__(self, symbol)->None :
        config = config_singleton_a()
        current_date = datetime.date.today()
        date = current_date.strftime('%Y-%m-%d')
        self.api_config = config.load_config()["FmpApi"]
        query = f"historical-price-full/{symbol}?from={self.api_config['from_date']}&to={date}&"
        super().__init__(query)
    
class Historical_market_cap(GetApi):
    """
    This class just needs to fill in the details of the query string for Historical market cap data. The Base class 
    takes care of all the execution of the rest of the functionality.

    we are passing the GetApi class object as a parameter for this class. 

    constructor is defined by using the __init__() fucntion to pass the query_string.

    Here, query_string contains the symbol of the company and the limit parameter (check the API documentation and source code for more details). 
    """

    def __init__(self, symbol)->None:
        query = "historical-market-capitalization/" + symbol + "?limit=2000&"
        super().__init__(query)

class Daily_prices(GetApi):
    """
    This class just needs to fill in the details of the query string for Daily prices. The Base class 
    takes care of all the execution of the rest of the functionality.

    we are passing the GetApi class object as a parameter for this class. 

    constructor is defined by using the __init__() fucntion to pass the query_string.

    Here, query_string contains the string 'quote?' along with the symbol of the company (check the API documentation and source code for more details). 
    """
    
    def __init__(self, symbol)->None :
        query = "quote/" + symbol +"?"
        super().__init__(query)

