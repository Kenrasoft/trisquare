from core.configuration.config import Config
from pulse.fmpapi.get_api import GetApi

import requests


class Global_stocks(GetApi):
    def __init__(self)->None:
        super().__init__("stock/list?")

class Historical_prices(GetApi):
    def __init__(self, symbol)->None :

        query = "historical-price-full/" + symbol + "?from=2017-01-01&to=2023-09-07&"
        current_date = datetime.date.today()
<<<<<<< Updated upstream
        date_str = current_date.strftime('%Y-%m-%d')
        query = "historical-price-full/" + symbol + "?from=2017-01-01&to=" + date_str + "&"
=======
        date = current_date.strftime('%Y-%m-%d')
        from_date = super().get_from_date
        query = f"historical-price-full/{symbol}?from={from_date}&to={date}&"
        super().__init__(query)
    
class Historical_market_cap(GetApi):
    def __init__(self, symbol)->None:
        query = "historical-market-capitalization/" + symbol + "?limit=2000&"
        super().__init__(query)

class Daily_prices(GetApi):
    def __init__(self, symbol)->None :
        query = "quote/" + symbol +"?"
        super().__init__(query)