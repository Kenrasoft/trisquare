from pulse.fmpapi.get_api import GetApi


class SP500(GetApi):
# The class just need to fill in the details of the query string for SP500. The Base class 
# takes care of all the execution of the rest of the functionality

    def __init__(self)-> None:
        super().__init__("sp500_constituent?")

class Nasdaq(GetApi):
# The class just need to fill in the details of the query string for NASDAQ. The Base class
# takes care of all the execution of the rest of the functionality

    def __init__(self)->None :
        super().__init__("nasdaq_constituent?")

class Dowjones(GetApi):
# The class just need to fill in the details of the query string for DOWJONES. The Base class
# takes care of all the execution of the rest of the functionality
    def __init__(self)->None :
        super().__init__("dowjones_constituent?")

