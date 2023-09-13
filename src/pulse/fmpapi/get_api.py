from core.configuration.config import Config
import requests

class GetApi:
# Access Financial Modeling Prep APIs
# It constructs the query string depending on the API and fetches the data
# The data will be retured from the API is in the JSON format
# The class is the base class for all the APIs. It does all the functionality of building the URL
# and fetches the data.
# All the sub classes just needs to provide the query string depending on the API. 

    config = Config()
    def __init__(self, query_string) -> None:
        self.api_config = GetApi.config.load_config()['FmpApi']
        self.api_response = None
        self.query_string = query_string
    
    def get_uri(self):
        return self.api_config['uri']
    
    def get_api_key(self):
        return self.api_config['key']
    
    def get_url(self):
        return self.get_uri() + self.query_string + self.get_api_key()
    
    def get_from_date(self):
        return self.api_config['from_date']
    
    def fetch(self):
        url = self.get_url()
        response = requests.get(url)
        jsondata = response.json()
        return jsondata


