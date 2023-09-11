# from pulse.fmpapi.get_api import Historicprices
# from pulse.fmpapi.get_api import Historic_market_cap

# class Combine:

#     def historic_price_marketcap(self):
#         historic_price_api = Historicprices()
#         Historic_price_json_data = historic_price_api.fetch()

#         historic_marketcap_api = Historic_market_cap()
#         Historic_marketcap_json_data = historic_marketcap_api.fetch()

#         symbol = Historic_price_json_data['symbol']

#         # Convert the list of dictionaries into dictionaries with date as keys
#         market_cap_dict = {entry["date"]: entry for entry in Historic_marketcap_json_data}
#         print(market_cap_dict)
#         price_dict = {entry["date"]: entry for entry in Historic_price_json_data["historical"]}
#         print(price_dict)

#         # Merge the two dictionaries using the common key (date) and include the 'symbol'
#         merged_data = [{**price_dict[date], "symbol": symbol, "marketCap": market_cap_dict[date]["marketCap"]} for date in set(price_dict) & set(market_cap_dict)]

#         return merged_data
    
from pulse.fmpapi.get_api import Historicprices
from pulse.fmpapi.get_api import Historic_market_cap

class Combine:

    def historic_price_marketcap(self):
        historic_price_api = Historicprices()
        Historic_price_json_data = historic_price_api.fetch()

        historic_marketcap_api = Historic_market_cap()
        Historic_marketcap_json_data = historic_marketcap_api.fetch()

        symbol = Historic_price_json_data['symbol']

        # Create a dictionary with date as keys for market cap data
        market_cap_dict = {entry["date"]: entry["marketCap"] for entry in Historic_marketcap_json_data}

        # Merge the two datasets using the common key (date) and include the 'symbol'
        merged_data = []
        
        for entry in Historic_price_json_data["historical"]:
            date = entry["date"]
            market_cap = market_cap_dict.get(date)  # Lookup market cap by date
            entry["symbol"] = symbol
            entry["marketCap"] = market_cap
            merged_data.append(entry)

        return merged_data
