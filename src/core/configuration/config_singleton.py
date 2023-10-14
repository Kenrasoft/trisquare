"""
We may want to have a single instance of the configuration file to avoid reading the configurational settings from files multiple times.
"""

import json

class config_singleton_a:
    """
    This class is used to define two methos __new__() and load_config()
    """
    _instance = None

    def __new__(cls):
        """
        Ensures that only one instance of the class exists.
    	"""
        
        if cls._instance is None:
            cls._instance = super(config_singleton_a, cls).__new__(cls)
            cls._instance.load_config()
        return cls._instance
    
    def load_config(self):
        """
        Loading the configuration settings from config.json file.
	    """
        
        try:          
            with open('./core/configuration/config.json', 'r') as file:
                self.config = json.load(file)
        except FileNotFoundError:
            print(f"Configuration file 'config.json' not found.")
            self.config = {}

        return self.config
    

