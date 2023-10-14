"""
The purpose of this index_companies_repo.py file is to create base classes for the index companies.

This module imports PulseDB_Base class from pulse.repository.pulsedb_base.py
"""

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, DateTime
from pulse.repository.pulsedb_base import PulseDB_Base

Base = declarative_base()


class SP500_table(Base, PulseDB_Base):
    """
    Entity class for the DB table SP500.
    
    Helps in loading the data into SP500 table by creating instances (objects for the class).
    
    :param Base: with the help of SQL Alchemy's ORM features, we generate the Base class object using the declarative_base() fucntion which is helpful to define the columns and for creating instances.  
    :param PulseDB_Base: we are passing the PulseDB_Base class object as a parameter for this class to override the convert() method.
    """

    __tablename__ = 'sp500'
    symbol = Column(String, primary_key=True)
    company_name = Column(String)
    sector = Column(String)
    subsector = Column(String)
    headquarter = Column(String)
    datefirstadded = Column(String)
    cik = Column(String)
    founded = Column(String)
    base = Base

    def getBase(self):
        return Base

    def convert(self, element):
        """
        Takes each key-value pair in the json data returned from the API and initializes an instance of the class SP500_table.
        
        :param element: One element in the JSON data.

        :return: row, which is the object of SP500_table class to the load_data() function in pulsedb_base.py which then adds this row into the data base table.
        """

        row = SP500_table(
                symbol=element["symbol"],
                company_name=element["name"],
                sector=element["sector"],
                subsector=element["subSector"],
                headquarter=element["headQuarter"],
                datefirstadded=element["dateFirstAdded"],
                cik=element["cik"],
                founded=element["founded"]
            )
        return row


class NASDAQ_table(Base,PulseDB_Base):
    """
    Entity class for the DB table nasdaq.
    
    Helps in loading the data into nasdaq table by creating instances (objects for the class).
    
    :param Base: with the help of SQL Alchemy's ORM features, we generate the Base class object using the declarative_base() fucntion which is helpful to define the columns and for creating instances.
    :param PulseDB_Base: we are passing the PulseDB_Base class object as a parameter for this class to override the convert() method.
    """

    __tablename__ = 'nasdaq'
    symbol = Column(String, primary_key=True)
    company_name = Column(String)
    sector = Column(String)
    subsector = Column(String)
    headquarter = Column(String)
    cik = Column(String)
    founded = Column(DateTime)
    
    def getBase(self):
        return Base
    
    def convert(self, element):
        """
        Takes each key-value pair in the json data returned from the API and initializes an instance of the class NASDAQ_table.
        
        :param element: One element in the JSON data.

        :return: row, which is the object of NASDAQ_table class to the load_data() function in pulsedb_base.py which then adds this row into the data base table.
        """

        row = NASDAQ_table(
            symbol=element["symbol"],
            company_name=element["name"],
            sector=element["sector"],
            subsector=element["subSector"],
            headquarter=element["headQuarter"],
            cik=element["cik"],
            founded=element["founded"]
        )
        return row

class DOWJONES_table(Base, PulseDB_Base):
    """
    Entity class for the DB table dowjones.
     
    Helps in loading the data into dowjones table by creating instances (objects for the class).
    
    :param Base: with the help of SQL Alchemy's ORM features, we generate the Base class object using the declarative_base() fucntion which is helpful to define the columns and for creating instances.  
    :param PulseDB_Base: we are passing the PulseDB_Base class object as a parameter for this class to override the convert() method.
    """

    __tablename__ = 'dowjones'
    symbol = Column(String, primary_key=True)
    company_name = Column(String)
    sector = Column(String)
    subsector = Column(String)
    headquarter = Column(String)
    datefirstadded = Column(DateTime)
    cik = Column(String)
    founded = Column(DateTime)

    def getBase(self):
        return Base

    def convert(self, element):
        """
        Takes key value pair in the json data returned from the API and initializes an instance of the class DOWJONES_table.
        
        :param element: One element in the JSON data.
        
        :return: row, which is the object of DOWJONES_table class to the load_data() function in pulsedb_base.py which then adds this row into the data base table.
        """
        
        row = DOWJONES_table(
            symbol=element["symbol"],
            company_name=element["name"],
            sector=element["sector"],
            subsector=element["subSector"],
            headquarter=element["headQuarter"],
            datefirstadded=element["dateFirstAdded"],
            cik=element["cik"],
            founded=element["founded"]
        )
        return row
    
