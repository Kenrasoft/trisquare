"""
The purpose this dataloader.py file is to load all the FMP Api data to pulse.

This module imports FmpApiToDatabase Class from the file pulse.integration.fmpapi_to_db.
"""

from pulse.integration.fmpapi_to_db import FmpApiToDatabase


FmpApiToDatabase.load_index_companies()

FmpApiToDatabase.load_global_stocks()

FmpApiToDatabase.load_historical_prices()

FmpApiToDatabase.load_daily_prices()
