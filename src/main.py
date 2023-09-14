from pulse.integration.fmpapi_to_db import FmpApiToDatabase

FmpApiToDatabase.load_index_companies()

FmpApiToDatabase.load_global_stocks()

FmpApiToDatabase.load_historical_prices()

FmpApiToDatabase.load_daily_prices()
