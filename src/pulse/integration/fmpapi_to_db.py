from pulse.fmpapi.index_companies import SP500
from pulse.fmpapi.index_companies import Nasdaq
from pulse.fmpapi.index_companies import Dowjones
from pulse.fmpapi.stock_prices import Global_stocks

from pulse.fmpapi.stock_prices import Historical_prices
from pulse.fmpapi.stock_prices import Historical_market_cap
from pulse.fmpapi.stock_prices import Daily_prices

# from pulse.fmpapi.get_api import daily_prices


# from pulse.fmpapi.get_api import Global_etfs
from pulse.repository.index_companies import SP500_table
from pulse.repository.index_companies import NASDAQ_table
from pulse.repository.index_companies import DOWJONES_table
from pulse.repository.stock_prices import Global_stocks_table
from pulse.repository.stock_prices import Historical_prices_table
from pulse.repository.stock_prices import Daily_prices_table


# from pulse.combine.combine import Combine

class FmpApiToDatabase():
# Integration layer to extract the FMPAPI data and load into . 
# This data is passed to the tables for loading. 
# Mainly focus on loading all the index companies from SP500, NASDAQ and DOWJONES

    def load_SP500_companies():

        sp500_api = SP500()
        sp500_json_data = sp500_api.fetch()
        print("Fetched sp500 json data from API")

        sp500_repo = SP500_table()
        # sp500.create_table(sp500_repo.getBase())
        sp500_repo.load_data(sp500_json_data)
        print("loaded sp500 API data into sp500 table")

    def load_Nasdaq_companies():

        nasdaq_api = Nasdaq()
        nasdaq_json_data = nasdaq_api.fetch()
        print("Fetched Nasdaq json data from API")

        nasdaq_repo = NASDAQ_table()
        # nasdaq_repo.create_table(nasdaq_repo.getBase())
        nasdaq_repo.load_data(nasdaq_json_data)
        print("loaded Nasdaq API data into Nasdaq table")

    def load_Dowjones_companies():
        dowjones_api = Dowjones()
        dowjones_json_data = dowjones_api.fetch()
        print("Fetched Dowjones json data from API")

        dowjones_repo = DOWJONES_table()
        # dowjones_repo.create_table(dowjones_repo.getBase())
        dowjones_repo.load_data(dowjones_json_data)
        print("loaded Dowjones API data into Dowjones table")

    def load_global_stocks():
        global_stocks_api = Global_stocks()
        global_stocks_json_data = global_stocks_api.fetch()
        print("Fetched global stocks json data from API")

        global_stocks_repo = Global_stocks_table()
        # globalstocks_repo.create_table(globalstocks_repo.getBase())
        global_stocks_repo.load_data(global_stocks_json_data)
        print("loaded Global stock API data into globalstocks table")

    def load_index_companies():
        FmpApiToDatabase.load_SP500_companies()
        FmpApiToDatabase.load_Nasdaq_companies()
        FmpApiToDatabase.load_Dowjones_companies()

    

    def load_historical_prices():
    #     # Get historic stock prices
        symbols = SP500_table().get_symbols()
        def fetch_and_process_data(company_symbol):

<<<<<<< Updated upstream
        symbol = "MSFT"
        historical_price_api = Historical_prices(symbol)
        historical_price_json_data = historical_price_api.fetch()

    #     # Get historic Makert cap 
        historical_marketcap_api = Historical_market_cap(symbol)
        historical_marketcap_json_data = historical_marketcap_api.fetch()

        symbol = historical_price_json_data['symbol']

    # Create a dictionary with date as keys for market cap data
        market_cap_dict = {element["date"]: element["marketCap"] for element in historical_marketcap_json_data}

=======
<<<<<<< Updated upstream
        symbols = SP500_table()
>>>>>>> Stashed changes
        historical_price_with_marketcap = []
        for element in historical_price_json_data["historical"]:
            date = element["date"]
            market_cap = market_cap_dict.get(date)  # Lookup market cap by date
            element["symbol"] = symbol
            element["marketCap"] = market_cap
            historical_price_with_marketcap.append(element)
            print(f"Element: {element}")    

        print(f"Fetched Historical stock price json data from API for symbol: {symbol}")

        historical_prices_repo = Historical_prices_table()
        historical_prices_repo.load_data(historical_price_with_marketcap)

<<<<<<< Updated upstream
        print(f"loaded Historical stock prices API data into Historical price table for symbol: {symbol}")
=======
        # Create a dictionary with date as keys for market cap data
            market_cap_dict = {element["date"]: element["marketCap"] for element in historical_marketcap_json_data}

            
            for element in historical_price_json_data["historical"]:
                date = element["date"]
                market_cap = market_cap_dict.get(date)  # Lookup market cap by date
                element["symbol"] = symbol
                element["marketCap"] = market_cap
                historical_price_with_marketcap.append(element)
                #print(f"Element: {element}")    

            print(f"Fetched Historical stock price json data from API for symbol: {symbol}")

            historical_prices_repo = Historical_prices_table()
            historical_prices_repo.load_data(historical_price_with_marketcap)

            print(f"loaded Historical stock prices API data into Historical price table for symbol: {symbol}")
=======
            historical_price_api = Historical_prices(company_symbol)
            historical_marketcap_api = Historical_market_cap(company_symbol)

            historical_price_json_data = historical_price_api.fetch()
            historical_marketcap_json_data = historical_marketcap_api.fetch()

            symbol = historical_price_json_data['symbol']

            market_cap_dict = {element["date"]: element["marketCap"] for element in historical_marketcap_json_data}
            
            historical_price_with_marketcap = []
            for element in historical_price_json_data["historical"]:
                date = element["date"]
                market_cap = market_cap_dict.get(date)
                element["symbol"] = symbol
                element["marketCap"] = market_cap
                historical_price_with_marketcap.append(element)

            print(f"Fetched and processed data for symbol: {symbol}")

            historical_prices_repo = Historical_prices_table()
            historical_prices_repo.load_data(historical_price_with_marketcap)

            print(f"Loaded data into Historical prices table for symbol: {symbol}")    
        # Use ThreadPoolExecutor to fetch and process data concurrently
        with ThreadPoolExecutor(max_workers=10) as executor:
            executor.map(fetch_and_process_data, symbols)

>>>>>>> Stashed changes
>>>>>>> Stashed changes


    def load_daily_prices():
        
        # Fetch SP500 table and get teh list of symbols
        symbol = "MSFT"
        daily_prices_api = Daily_prices(symbol)
        daily_prices_json_data = daily_prices_api.fetch()

        print(f"Fetched stock prices json data from API for symbol: {symbol}")

        daily_prices_repo = Daily_prices_table()
        daily_prices_repo.load_data(daily_prices_json_data)

<<<<<<< Updated upstream
        print(f"loaded stock prices API data into stock price table for symbol: {symbol}")
=======
<<<<<<< Updated upstream
            print(f"loaded stock prices API data into stock price table for symbol: {symbol}")
=======
            print(f"loaded stock prices API data into stock price table for symbol: {symbol}")
>>>>>>> Stashed changes
>>>>>>> Stashed changes
