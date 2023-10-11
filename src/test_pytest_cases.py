from test_functions import singleton
from core.configuration.config_singleton import config_singleton
from pulse.fmpapi.index_companies_api import SP500
from pulse.fmpapi.index_companies_api import Nasdaq
from pulse.fmpapi.index_companies_api import Dowjones
from pulse.fmpapi.stock_prices_api import Historical_prices
from pulse.integration.fmpapi_to_db import FmpApiToDatabase
from pulse.fmpapi.stock_prices_api import Daily_prices
from pulse.fmpapi.stock_prices_api import Historical_market_cap

import requests
import pandas as pd
from datetime import datetime,timedelta

def test_config_single():
    object1 = config_singleton()
    object1.load_config()
    object2 = config_singleton()
    object2.load_config()
    assert singleton(object1,object2) == True


def test_sp500_api():
    
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
    current_date = datetime.now()
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
    response = requests.get("https://financialmodelingprep.com/api/v3/quote/AAPL?apikey=304459a7a227a31923b63192971bc245")
    # Check that the API response was successful
    assert response.status_code == 200

    daily_prices_api = Daily_prices("AAPL")
    daily_prices_json_data = daily_prices_api.fetch()

    df = pd.DataFrame(daily_prices_json_data)
    
    current_date = datetime.now()
    c_date = current_date.strftime("%Y-%m-%d")
    
    #latest_date = df['date_time'].max()
    timestamp = df["timestamp"]
    timestamp = int(timestamp.iloc[0])
    date = datetime.fromtimestamp(timestamp)
    latest_date = date.date()
    latest_date = latest_date.strftime("%Y-%m-%d")

    assert latest_date == c_date

def test_historicmarketcap_api():
    response = requests.get("https://financialmodelingprep.com/api/v3/historical-market-capitalization/AAPL?limit=2000&apikey=304459a7a227a31923b63192971bc245")
    # Check that the API response was successful
    assert response.status_code == 200

    current_date = datetime.now()
    previous_date = current_date - timedelta(days=1)
    date = current_date.strftime("%Y-%m-%d")
    prv_date = previous_date.strftime("%Y-%m-%d")

    historical_market_api = Historical_market_cap("AAPL")
    historical_market_json_data = historical_market_api.fetch()    

    df = pd.DataFrame(historical_market_json_data)
    df_date = df['date'].max()

    assert date == df_date or prv_date == df_date