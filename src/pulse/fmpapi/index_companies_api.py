"""
The purpose of this index_companies_api.py file is to provide the query_strings of the index companies - sp500, Nasdaq and Dowjones to the GetApi class in the get_api.py module.

This module imports the GetApi class from pulse.fmpapi.get_api
"""

from pulse.fmpapi.get_api import GetApi

class SP500(GetApi):
    """
    This class just needs to fill in the details of the query string for SP500. The Base class 
    takes care of all the execution of the rest of the functionality.

    we are passing the GetApi class object as a parameter for this class. 

    constructor is defined by using the __init__() fucntion to pass the query_string "sp500_constituent?".
    """

    def __init__(self)-> None:
        super().__init__("sp500_constituent?")

class Nasdaq(GetApi):
    """
    This class just needs to fill in the details of the query string for Nasdaq. The Base class 
    takes care of all the execution of the rest of the functionality.

    we are passing the GetApi class object as a parameter for this class. 

    constructor is defined by using the __init__() fucntion to pass the query_string "nasdaq_constituent?".
    """

    def __init__(self)->None :
        super().__init__("nasdaq_constituent?")

class Dowjones(GetApi):
    """
    This class just needs to fill in the details of the query string for Dowjones. The Base class 
    takes care of all the execution of the rest of the functionality.

    we are passing the GetApi class object as a parameter for this class. 

    constructor is defined by using the __init__() fucntion to pass the query_string "dowjones_constituent?".
    """
    
    def __init__(self)->None :
        super().__init__("dowjones_constituent?")

