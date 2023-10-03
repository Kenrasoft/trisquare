from pulse.integration.fmpapi_to_db import FmpApiToDatabase
# this is the main file to load all the FMP Api data to pulse.

#FmpApiToDatabase.load_index_companies()

FmpApiToDatabase.load_global_stocks()

FmpApiToDatabase.load_historical_prices()

FmpApiToDatabase.load_daily_prices()
