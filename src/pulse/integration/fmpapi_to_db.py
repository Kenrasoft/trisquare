
from pulse.fmpapi.index_companies_api import SP500
from pulse.fmpapi.index_companies_api import Nasdaq
from pulse.fmpapi.index_companies_api import Dowjones
from pulse.fmpapi.stock_prices_api import Global_stocks
from pulse.fmpapi.company_analysis_api import Comp_estimates
from pulse.fmpapi.company_analysis_api import Comp_ratings

from pulse.fmpapi.stock_prices_api import Historical_prices
from pulse.fmpapi.stock_prices_api import Historical_market_cap
from pulse.fmpapi.stock_prices_api import Daily_prices
from pulse.fmpapi.company_analysis_api import Comp_recom


from pulse.repository.index_companies_repo import SP500_table
from pulse.repository.index_companies_repo import Nasdaq_table
from pulse.repository.index_companies_repo import Dowjones_table
from pulse.repository.stock_prices_repo import Global_stocks_table
from pulse.repository.stock_prices_repo import Historical_prices_table
from pulse.repository.stock_prices_repo import Daily_prices_table
from pulse.repository.company_analysis_repo import Comp_estimates_table
from pulse.repository.company_analysis_repo import Comp_ratings_table
from pulse.repository.company_analysis_repo import Comp_recom_table

from pulse.repository.queries import Queries
from concurrent.futures import ThreadPoolExecutor


class FmpApiToDatabase():
# Integration layer to extract the FMPAPI data and load into . 
# This data is passed to the tables for loading. 
# Mainly focus on loading all the index companies from SP500, NASDAQ and DOWJONES

# {classname}.create_table({class_repo}.getBase()) is used to create table for class. 
# Generally we run it when we dont have a table createdin pulse DB.

    def load_SP500_companies():

        sp500_api = SP500()
        sp500_json_data = sp500_api.fetch()
        print("Fetched sp500 json data from API")

        sp500_repo = SP500_table()
        # The below line which is commented is used to create table based on class
        # sp500.create_table(sp500_repo.getBase())
        sp500_repo.load_data(sp500_json_data)
        print("loaded sp500 API data into sp500 table")

    def load_Nasdaq_companies():

        nasdaq_api = Nasdaq()
        nasdaq_json_data = nasdaq_api.fetch()
        print("Fetched Nasdaq json data from API")

        nasdaq_repo = Nasdaq_table()
        # The below line which is commented is used to create table based on class
        # nasdaq_repo.create_table(nasdaq_repo.getBase())
        nasdaq_repo.load_data(nasdaq_json_data)
        print("loaded Nasdaq API data into Nasdaq table")

    def load_Dowjones_companies():
        dowjones_api = Dowjones()
        dowjones_json_data = dowjones_api.fetch()
        print("Fetched Dowjones json data from API")

        dowjones_repo = Dowjones_table()
        # The below line which is commented is used to create table based on class
        # dowjones_repo.create_table(dowjones_repo.getBase())
        dowjones_repo.load_data(dowjones_json_data)
        print("loaded Dowjones API data into Dowjones table")

    def load_index_companies():
        #This method is used to load all the index stocks.
        FmpApiToDatabase.load_SP500_companies()
        FmpApiToDatabase.load_Nasdaq_companies()
        FmpApiToDatabase.load_Dowjones_companies()


    def load_global_stocks():
        global_stocks_api = Global_stocks()
        global_stocks_json_data = global_stocks_api.fetch()
        print("Fetched global stocks json data from API")

        global_stocks_repo = Global_stocks_table()
        # The below line which is commented is used to create table based on class
        # globalstocks_repo.create_table(globalstocks_repo.getBase())
        global_stocks_repo.load_data(global_stocks_json_data)
        print("loaded Global stock API data into globalstocks table")

    
    def load_historical_prices():
        FmpApiToDatabase.load_historical_prices_no_threading()

    def load_historical_prices_with_threading():
        # We are here getting historic prices of SP500 stocks. So fetching the symbols 
        # of SP500
        symbols = Queries().get_symbols()

        # As this is going to make lot of calls, the threading is introduced to make the processing faster
        with ThreadPoolExecutor(max_workers=15) as executor:
            executor.map(FmpApiToDatabase.load_historical_prices_for_symbol, symbols)

    # Fetch the historical market cap data and pricing information
    # and then load the data into database 
    def load_historical_prices_for_symbol(company_symbol): 
        
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

    def load_comp_estimates():
        # We are here getting company estimates of SP500 stocks. So fetching the symbols 
        # of SP500
        symbols = Queries()
        for symbol in symbols.get_symbols():
            comp_estimates_api = Comp_estimates(symbol)
            comp_estimates_json_data = comp_estimates_api.fetch()

            print(f"Fetched analyst estimates json data from API for symbol: {symbol}")

            analyst_estimates_repo = Comp_estimates_table()
            analyst_estimates_repo.load_data(comp_estimates_json_data)

            print(f"loaded analyst estimates API data into comp_estimates table for symbol: {symbol}")
            

    def load_comp_ratings():
            # We are here getting company ratings of SP500 stocks. So fetching the symbols 
            # of SP500
        symbols = Queries()
        for symbol in symbols.get_symbols():
            
            Comp_ratings_api = Comp_ratings(symbol)
            Comp_ratings_json_data = Comp_ratings_api.fetch()

            print(f"Fetched analyst estimates json data from API for symbol: {symbol}")

            analyst_ratings_repo = Comp_ratings_table()
            analyst_ratings_repo.load_data(Comp_ratings_json_data)

            print(f"loaded analyst ratings API data into Comp_Ratings table for symbol: {symbol}")
            

    def load_comp_recom():
        # Getting analyst company recommendations for sp500 stocks. 
        # Fetching the symbols of SP500
        symbols=Queries()
        for symbol in symbols.get_symbols():
            comp_recom_api = Comp_recom(symbol)
            # Calling FMP API to Get analyst company recommendations for each symbol. 
            comp_recom_json_data = comp_recom_api.fetch()

            print(f"Fetched company recommendation json data from API for symbol: {symbol}")

            comp_recom_repo = Comp_recom_table()
            # loading company recommendations for each symbol
            comp_recom_repo.load_data(comp_recom_json_data)

            print(f"loaded company recommendation API data into comp_recom table for symbol: {symbol}")
        
    def load_company_analysis():
        #This method is used to load all the index stocks.
        FmpApiToDatabase.load_comp_recom()
        FmpApiToDatabase.load_comp_ratings()
        FmpApiToDatabase.load_comp_estimates()

