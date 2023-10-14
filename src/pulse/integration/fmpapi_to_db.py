"""
The purpose of this fmpapi_to_db.py file is to integrate the functionalities between the fmpapi (api related) and the repository (data base related) i.e., to serve as a connection between sending the data accessed using the API to the data base.

This module imports all the required classes (look into source code link here) from both the fmpapi and repository folders.

"""

from pulse.fmpapi.index_companies_api import SP500
from pulse.fmpapi.index_companies_api import Nasdaq
from pulse.fmpapi.index_companies_api import Dowjones
from pulse.fmpapi.stock_prices_api import Global_stocks

from pulse.fmpapi.stock_prices_api import Historical_prices
from pulse.fmpapi.stock_prices_api import Historical_market_cap
from pulse.fmpapi.stock_prices_api import Daily_prices


from pulse.repository.index_companies_repo import SP500_table
from pulse.repository.index_companies_repo import NASDAQ_table
from pulse.repository.index_companies_repo import DOWJONES_table
from pulse.repository.stock_prices_repo import Global_stocks_table
from pulse.repository.stock_prices_repo import Historical_prices_table
from pulse.repository.stock_prices_repo import Daily_prices_table
from pulse.repository.queries import Queries
from concurrent.futures import ThreadPoolExecutor


class FmpApiToDatabase():
    """
    Integration layer to extract the FMPAPI data and load it into the database.

    All the functions under this class load the data from the API using the fetch() function in get_api.py and load that data into respective tables using the load_data() function in the pulsedb_base.py.

    """

# {classname}.create_table({class_repo}.getBase()) is used to create table for class. 
# Generally we run it when we dont have a table createdin pulse DB.

    def load_SP500_companies():
        """
        This function is to load the sp500 companies data into the data base (SP500_table).

        """

        sp500_api = SP500()
        sp500_json_data = sp500_api.fetch()
        print("Fetched sp500 json data from API")

        sp500_repo = SP500_table()
        # The below line which is commented is used to create table based on class
        # sp500.create_table(sp500_repo.getBase())
        sp500_repo.load_data(sp500_json_data)
        print("loaded sp500 API data into sp500 table")

    def load_Nasdaq_companies():
        """
        This function is to load the Nasdaq companies data into the data base (NASDAQ_table).

        """

        nasdaq_api = Nasdaq()
        nasdaq_json_data = nasdaq_api.fetch()
        print("Fetched Nasdaq json data from API")

        nasdaq_repo = NASDAQ_table()
        # The below line which is commented is used to create table based on class
        # nasdaq_repo.create_table(nasdaq_repo.getBase())
        nasdaq_repo.load_data(nasdaq_json_data)
        print("loaded Nasdaq API data into Nasdaq table")

    def load_Dowjones_companies():
        """
        This function is to load the Dowjones companies data into the data base (DOWJONES_table).

        """

        dowjones_api = Dowjones()
        dowjones_json_data = dowjones_api.fetch()
        print("Fetched Dowjones json data from API")

        dowjones_repo = DOWJONES_table()
        # The below line which is commented is used to create table based on class
        # dowjones_repo.create_table(dowjones_repo.getBase())
        dowjones_repo.load_data(dowjones_json_data)
        print("loaded Dowjones API data into Dowjones table")

    def load_index_companies():
        """
        This method is used to load all the stocks of index companies.

        """
        
        FmpApiToDatabase.load_SP500_companies()
        FmpApiToDatabase.load_Nasdaq_companies()
        FmpApiToDatabase.load_Dowjones_companies()


    def load_global_stocks():
        """
        This function is to load the gobal stocks data into the data base (Global_stocks_table).

        """

        global_stocks_api = Global_stocks()
        global_stocks_json_data = global_stocks_api.fetch()
        print("Fetched global stocks json data from API")

        global_stocks_repo = Global_stocks_table()
        # The below line which is commented is used to create table based on class
        # globalstocks_repo.create_table(globalstocks_repo.getBase())
        global_stocks_repo.load_data(global_stocks_json_data)
        print("loaded Global stock API data into globalstocks table")

    
    def load_historical_prices():
        """
        This function is to load the historical prices data, just calls the function load_historical_prices_no_threading().

        """

        FmpApiToDatabase.load_historical_prices_no_threading()

    def load_historical_prices_with_threading():
        """
        Fetching historical data is going to make lot of calls to the API. So, threading is introduced to make the processing faster.

        Here, we are just getting historic prices of SP500 stocks using the symbols of SP500 companies.

        It calls the function load_historical_prices_for_symbol() to get the data.
        
        we are not actually using it for now, but we might use it later.
        """

        symbols = Queries().get_symbols()

        # As this is going to make lot of calls, the threading is introduced to make the processing faster
        with ThreadPoolExecutor(max_workers=15) as executor:
            executor.map(FmpApiToDatabase.load_historical_prices_for_symbol, symbols)


    def load_historical_prices_for_symbol(company_symbol): 
        """
        Fetch the historical market cap data and pricing information and then load the data into database.

        :param company_symbol: Symbols of sp500 companies passed  by the load_historical_prices_with_threading() method.

        """
        
        historical_price_api = Historical_prices(company_symbol)
        historical_marketcap_api = Historical_market_cap(company_symbol)

        print(f"Getting historical data for symbol: {company_symbol}")
        historical_price_json_data = historical_price_api.fetch()
        historical_marketcap_json_data = historical_marketcap_api.fetch()
    
        if len(historical_price_json_data) > 0 and len(historical_marketcap_json_data) > 0:
            symbol = historical_price_json_data['symbol']
            market_cap_dict = {element["date"]: element["marketCap"] for element in historical_marketcap_json_data}
            historical_price_with_marketcap = []

            number = 0
            for element in historical_price_json_data["historical"]:
                date = element["date"]
                market_cap = market_cap_dict.get(date)
                element["symbol"] = symbol
                element["marketCap"] = market_cap
                historical_price_with_marketcap.append(element)

                historical_prices_repo = Historical_prices_table()
                historical_prices_repo.load_data(historical_price_with_marketcap)
                number = number + 1
                print(f"Loaded data into Historical prices table for the symbol: {symbol} on {date}")    
        else:
            print(f"Historical market data is not available for the symbol: {company_symbol} ")    

    def load_historical_prices_no_threading(): 
        """
        Used to load the historical prices.
        
        Does the same functionality as load_historical_prices_with_threading -- just that threading process is not involved in this.
        """

        symbols = Queries().get_symbols()
        for company_symbol in symbols: 
            
            historical_price_api = Historical_prices(company_symbol)
            historical_marketcap_api = Historical_market_cap(company_symbol)

            print(f"Getting historical data for symbol: {company_symbol}")
            historical_price_json_data = historical_price_api.fetch()
            historical_marketcap_json_data = historical_marketcap_api.fetch()
    
            if len(historical_price_json_data) > 0 and len(historical_marketcap_json_data) > 0:
                symbol = historical_price_json_data['symbol']
                market_cap_dict = {element["date"]: element["marketCap"] for element in historical_marketcap_json_data}
                historical_price_with_marketcap = []
                for element in historical_price_json_data["historical"]:
                    date = element["date"]
                    market_cap = market_cap_dict.get(date)
                    element["symbol"] = symbol
                    element["marketCap"] = market_cap
                    historical_price_with_marketcap.append(element)

                historical_prices_repo = Historical_prices_table()
                historical_prices_repo.load_data(historical_price_with_marketcap)

                print(f"Loaded data into Historical prices table for symbol: {symbol}")    
            else:
               print(f"Historical market data is not available for the symbol: {company_symbol} ")    

        


    def load_daily_prices():
        """
        This function is to load the daily prices of SP500 stocks data into the data base (Daily_prices_table).

        """
        
        # We are here getting daily prices of SP500 stocks. So fetching the symbols 
        # of SP500
        symbols = Queries()
        for symbol in symbols.get_symbols():
            daily_prices_api = Daily_prices(symbol)
            daily_prices_json_data = daily_prices_api.fetch()

            print(f"Fetched stock prices json data from API for symbol: {symbol}")

            daily_prices_repo = Daily_prices_table()
            daily_prices_repo.load_data(daily_prices_json_data)

            print(f"loaded stock prices API data into stock price table for symbol: {symbol}")
