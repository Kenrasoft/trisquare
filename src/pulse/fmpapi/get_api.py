"""
The purpose of this get_api.py file is to define the base class to access all the API's. The base class builds the URL and fetches the data from the API.

This module imports the config file (which stores details to access the API) from core.configuration.config.
"""

from core.configuration.config_singleton import config_singleton_a
import requests
import datetime
import time

class GetApi:
    """
    GetApi is the base class to access Financial Modeling Prep APIs.

    It constructs the query string depending on the API, does all the 
    functionality of building the URL and fetches the data from the API.

    All the sub classes (from index_companies_api.py or stock_prices_api.py in the current fmpapi module) just needs to provide the query string depending on the API.
    
    Attributes:
        query_string (str): The name of the string required to fetch specific data. For example, sp500_constituent? is the query string required to access data related to sp500 companies.    
    """

    # As per our subscription, we can make only 300 calls per minute. So if we exceed 300, then API doesn't respond. 
    # It's causing an error especially loading historical data for all the stocks. 
    # The below parameters are required for throttling the requests to FMP API

    # These are all class level variables to control the number of calls. Typically GetApi is instantiated for each API call
    # But we need to have a counter on number of calls made to API. So you need class variables to take care of this situation
    # We will be counting the number of calls across the app, and if it exceeds the limit, we will be sleeping for the rest of the time
    # and resume it, so we will not be missing tje calls.  
    #     
    TOTAL_CALLS_PER_MINUTE = 280
    MINUTE = 60
    completed_calls = 0
    timer = 0
    timer_start_time = datetime.datetime.now()

    def __init__(self, query_string) -> None:
        config = config_singleton_a()
        self.api_config = config.load_config()["FmpApi"]
        self.api_response = None
        self.query_string = query_string

    def get_uri(self):
        """
        Function to get the URI value mentioned in the configurations file.
        
        Returns:
            string: URI.
        """

        return self.api_config["uri"]

    def get_api_key(self):
        """
        Function to get the api_key value mentioned in the configurations file.
        
        Returns:
            string: api_key.
        """

        return self.api_config["key"]

    def get_url(self):
        """
        Function to generate the URL using URI, query_string and api_key.
        
        Returns:
            string: URL.
        """

        return self.get_uri() + self.query_string + self.get_api_key()

    def api_call(self):
        """
        Function to fetch the data from the API using URL and then covert the data into JSON format.
        
        Returns:
            json dictionary: response, it's the json data fetched from the api.
        """

        url = self.get_url()
        response = requests.get(url)
        jsondata = response.json()
        return jsondata

    def fetch(self):
        """
        Function to fetch the data in the json format from the api.

        Returns:
            You just call the throttle function in this and return the response.
        """

        return self.throttle(self.api_call)

    # Throttling the calls across the app
    def throttle(self, api):
        """
        As per our subscription, we can make only 300 calls per minute. 
        So if we exceed 300, then the API doesn't respond.

        throttle function is used to handle this issue.

        Args:
            api (json dictionary): data returned from the api_call method.

        Returns:
            json dictionary: response, it's the json data fetched from the api itself - after handling the issue mentioned above.
    
        """
        
        if GetApi.completed_calls > GetApi.TOTAL_CALLS_PER_MINUTE and GetApi.timer < GetApi.MINUTE:
            
            print(f"Total calls made so far : {GetApi.completed_calls}")
            sleep_time = GetApi.MINUTE - GetApi.timer
            print(f"Sleep time for : {sleep_time}")
            time.sleep(sleep_time)
            GetApi.completed_calls = 0
            
        api_begin_time = datetime.datetime.now()
        response = api()
        api_end_time = datetime.datetime.now()
        if GetApi.completed_calls == 0:
            GetApi.timer_start_time = api_begin_time

        GetApi.completed_calls = GetApi.completed_calls + 1
        
        time_diff = api_begin_time - GetApi.timer_start_time 
        GetApi.timer = int(time_diff.total_seconds())

        return response
        