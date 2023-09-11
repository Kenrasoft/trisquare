from pulse.fmpapi.get_api import SP500
from pulse.fmpapi.get_api import Nasdaq
from pulse.fmpapi.get_api import Dowjones
from pulse.fmpapi.get_api import Stockprices
from pulse.fmpapi.get_api import Historicprices
from pulse.fmpapi.get_api import Global_stocks
from pulse.fmpapi.get_api import Global_etfs
from pulse.repository.index_companies import SP500_table
from pulse.repository.index_companies import NASDAQ_table
from pulse.repository.index_companies import DOWJONES_table
from pulse.repository.stock_prices import Global_stocks_table
from pulse.repository.stock_prices import Global_etfs_table
from pulse.repository.stock_prices import Stock_prices_table
from pulse.repository.stock_prices import Historic_prices_table
from pulse.combine.combine import Combine

class Controller():
# Controller calls the FMPAPI and gets the JSON data. 
# This data is passed to the tables for loading. 
# Mainly focus on loading all the index companies from SP500, NASDAQ and DOWJONES

    def load_index_companies():
        # sp500_api = SP500()
        # sp500_json_data = sp500_api.fetch()
        # print("Fetched sp500 json data from API")

        # sp500_repo = SP500_table()
        # # sp500.create_table(sp500_repo.getBase())
        # sp500_repo.load_data(sp500_json_data)
        # print("loaded sp500 API data into sp500 table")


        # nasdaq_api = Nasdaq()
        # nasdaq_json_data = nasdaq_api.fetch()
        # print("Fetched Nasdaq json data from API")

        # nasdaq_repo = NASDAQ_table()
        # # nasdaq_repo.create_table(nasdaq_repo.getBase())
        # nasdaq_repo.load_data(nasdaq_json_data)
        # print("loaded Nasdaq API data into Nasdaq table")

        # dowjones_api = Dowjones()
        # dowjones_json_data = dowjones_api.fetch()
        # print("Fetched Dowjones json data from API")

        # dowjones_repo = DOWJONES_table()
        # # dowjones_repo.create_table(dowjones_repo.getBase())
        # dowjones_repo.load_data(dowjones_json_data)
        # print("loaded Dowjones API data into Dowjones table")


        # global_stocks_api = Global_stocks()
        # global_stocks_json_data = global_stocks_api.fetch()
        # print("Fetched global stocks json data from API")

        # global_stocks_repo = Global_stocks_table()
        # # globalstocks_repo.create_table(globalstocks_repo.getBase())
        # global_stocks_repo.load_data(global_stocks_json_data)
        # print("loaded Global stock API data into globalstocks table")


        # global_etfs_api = Global_etfs()
        # global_etfs_json_data = global_etfs_api.fetch()
        # print("Fetched global etf json data from API")

        # global_etfs_repo = Global_etfs_table()
        # #global_etfs_repo.create_table(global_etfs_repo.getBase())
        # global_etfs_repo.load_data(global_etfs_json_data)
        # print("loaded Global etf API data into global etf table")


        # stock_price_api = Stockprices()
        # stock_price_json_data = stock_price_api.fetch()
        # print("Fetched stock price json data from API")

        # stock_price_repo = Stock_prices_table()
        # # stock_price_repo.create_table(stock_price_repo.getBase())
        # stock_price_repo.load_data(stock_price_json_data)
        # print("loaded stock price API data into stockprices table")


        historic_combined = Combine()
        historic_price_marketcap_json_data = historic_combined.historic_price_marketcap()
        print("Fetched price, market cap together")




        

        historic_prices_repo = Historic_prices_table()
        historic_prices_repo.create_table(historic_prices_repo.getBase())
        historic_prices_repo.load_data(historic_price_marketcap_json_data)
        print("loaded prices_marktcap data into historicprices table")



        # historic_prices_api = Historicprices()
        # historic_prices_json_data = historic_prices_api.fetch()
        # print("Fetched price json data from API")


# from pulse.fmpapi.get_api import Historic_market_cap, Historicprices

# # Fetch data from Historic_market_cap API
# market_cap_api = Historic_market_cap()
# market_cap_data = market_cap_api.fetch()

# # Fetch data from Historicprices API
# historic_prices_api = Historicprices()
# historic_prices_data = historic_prices_api.fetch()

# Create a dictionary for market cap data with both date and symbol as keys
# market_cap_dict = {entry['date']: entry['marketCap'] for entry in market_cap_data}
# print('Market Cap Data: ', market_cap_dict)


# # Combine data from both dictionaries based on both date and symbol
# combined_data = {}

# for (symbol, date), market_cap in market_cap_dict.items():
#     if (symbol, date) in historic_prices_dict:
#         historic_data = historic_prices_dict[(symbol, date)]
#         historic_data['marketCap'] = market_cap
#         combined_data[(symbol, date)] = historic_data

# # Now combined_data contains the combined data with both date and symbol as keys
# print(combined_data)

