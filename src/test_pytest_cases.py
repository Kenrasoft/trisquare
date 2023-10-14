"""
The purpose of this module is to do testing using pytest for all the data under fmpapi module.
"""

from test_functions import test_config_singleton
from core.configuration.config_singleton import config_singleton_a
from pulse.fmpapi.index_companies_api import SP500
from pulse.fmpapi.index_companies_api import Nasdaq
from pulse.fmpapi.index_companies_api import Dowjones
from pulse.fmpapi.stock_prices_api import Historical_prices
from pulse.integration.fmpapi_to_db import FmpApiToDatabase
from pulse.fmpapi.stock_prices_api import Daily_prices
from pulse.fmpapi.stock_prices_api import Historical_market_cap

import requests
import pandas as pd
import datetime

def test_config_single():
    """
	create two instances of singleton class and comparing the instances to ensure that they refer to the same object.
    """

    object1 = config_singleton_a()
    object1.load_config()
    object2 = config_singleton_a()
    object2.load_config()
    assert test_config_singleton(object1,object2) == True


def test_sp500_api():
    """
   	check if the api link is working through http status code. 
    
    Also counting for number of unique symbols in sp500 table after fetching the json data from the api link.
    """
    
    response = requests.get("https://financialmodelingprep.com/api/v3/sp500_constituent?apikey=304459a7a227a31923b63192971bc245")
    # Check that the API response was successful
    assert response.status_code == 200

    sp500_api = SP500()
    sp500_json_data = sp500_api.fetch()

    df = pd.DataFrame(sp500_json_data)

        # Check the number of unique values in a specific column (e.g., "column_name")
    unique_values_count = df["symbol"].nunique()

    # Assert that the number of unique values meets your expectation
    expected_unique_values_count = 500  
    assert unique_values_count >= expected_unique_values_count

def test_nasdaq_api():
    """
    check if the api link is working through http status code. 

    Also counting for number of unique symbols in nasdaq table after fetching the json data from the api link.
    """
    
    response = requests.get("https://financialmodelingprep.com/api/v3/nasdaq_constituent?apikey=304459a7a227a31923b63192971bc245")
    # Check that the API response was successful
    assert response.status_code == 200

    nasdaq_api = Nasdaq()
    nasdaq_json_data = nasdaq_api.fetch()

    df = pd.DataFrame(nasdaq_json_data)

        # Check the number of unique values in a specific column (e.g., "column_name")
    unique_values_count = df["symbol"].nunique()

    # Assert that the number of unique values meets your expectation
    expected_unique_values_count = 100  
    assert unique_values_count >= expected_unique_values_count

def test_dowjones_api():
    """
    check if the api link is working through http status code. 		
    
    Also counting for number of unique symbols in dowjones table after fetching the json data from the api link.
    """
    
    response = requests.get("https://financialmodelingprep.com/api/v3/dowjones_constituent?apikey=304459a7a227a31923b63192971bc245")
    # Check that the API response was successful
    assert response.status_code == 200

    dowjones_api = Dowjones()
    dowjones_json_data = dowjones_api.fetch()

    df = pd.DataFrame(dowjones_json_data)

        # Check the number of unique values in a specific column (e.g., "column_name")
    unique_values_count = df["symbol"].nunique()

    # Assert that the number of unique values meets your expectation
    expected_unique_values_count = 30  
    assert unique_values_count >= expected_unique_values_count

def test_historical_api():
    """
    checking if the api link is working through http status code. 

    comparing if the current date is equal to the recent date in historical_api table, so that we know that the api link is providing the most recent data.
    """

    current_date = datetime.date.today()
    date = current_date.strftime("%Y-%m-%d")
    
    response = requests.get("https://financialmodelingprep.com/api/v3/historical-price-full/AAPL?from="+date+"&to="+date+"&apikey=304459a7a227a31923b63192971bc245")
    # Check that the API response was successful
    assert response.status_code == 200

    historical_prices_api = Historical_prices("AAPL")
    historical_prices_json_data = historical_prices_api.fetch()    

    df = pd.DataFrame(historical_prices_json_data)
    df_date = df['historical'][0]['date']

    assert date == df_date



def test_dailyprices_api():
    """
    checking if the api link is working through http status code. 

    comparing if the current date is equal to the recent date in dailyprices table, so that we know that the api link is providing the most recent data.
    """
    
    response = requests.get("https://financialmodelingprep.com/api/v3/quote/AAPL?apikey=304459a7a227a31923b63192971bc245")
    # Check that the API response was successful
    assert response.status_code == 200

    daily_prices_api = Daily_prices("AAPL")
    daily_prices_json_data = daily_prices_api.fetch()

    df = pd.DataFrame(daily_prices_json_data)
    
    current_date = datetime.date.today()
    
    #latest_date = df['date_time'].max()
    timestamp = df["timestamp"]
    timestamp = int(timestamp.iloc[0])
    date = datetime.datetime.fromtimestamp(timestamp)
    latest_date = date.date()

    assert latest_date == current_date

def test_historicmarketcap_api():
    """
    checking if the api link is working through http status code. 

    comparing if the current date is equal to the recent date in historicmarketcap_api table, so that we know that the api link is providing the most recent data.
    		"""
    response = requests.get("https://financialmodelingprep.com/api/v3/historical-market-capitalization/AAPL?limit=2000&apikey=304459a7a227a31923b63192971bc245")
    # Check that the API response was successful
    assert response.status_code == 200

    current_date = datetime.date.today()
    date = current_date.strftime("%Y-%m-%d")

    historical_market_api = Historical_market_cap("AAPL")
    historical_market_json_data = historical_market_api.fetch()    

    df = pd.DataFrame(historical_market_json_data)
    df_date = df['date'].max()

    assert date == df_date




historical_prices_api = Historical_prices("AAPL")
historical_prices_json_data = historical_prices_api.fetch()    

df = pd.DataFrame(historical_prices_json_data)

print (df)