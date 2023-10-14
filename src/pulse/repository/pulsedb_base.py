"""
The purpose of this pulsedb_base.py file is to load the data (row by row) into the data base tables.

This module imports DatabaseConnect from pulse.repository.database_connect to access the database connection.
"""

from pulse.repository.database_connect import DatabaseConnect
from sqlalchemy.exc import IntegrityError

class PulseDB_Base():
    """
    This class is used to handle database connections, loading the JSON data from API, adding rows to tables.
    """

    base = None
    def convert(self, element):
        """
        All the sub classes that inherits this PulseDB_Base Class can override this method convert() according to their specific requirements.
        
        :param element: One element in the JSON data.

        In the load_data() method below, we are calling this method convert(). 
        """

        pass

    def load_data(self, data): 
        """
        In this function, you use the 'with' to open the database session and then for each element in the JSON data, you pass it to conert() method which gives back an object() which can be added as a row in the database table. 

        we use error handling as well, If the row gets added succesfully - then, the transaction gets committed or else we rollback the transaction.

        :param data: data that is fetched from the API in the JSON format (dictionary).
        """

        db_connector = DatabaseConnect()
        session = db_connector.connect_db()
        with session() as s:
            for element in data:
                row = self.convert(element)
                try:
                    s.merge(row)
                    s.commit()
                except IntegrityError as e:
                    s.rollback()  # Roll back the transaction
            
    
    def create_table(self, base):
        """
        This method is to create the table using SQL Alchemy's way but we generally create tables using raw SQL queries so that we have better control of the underlying schema.
        """
        
        db_connector = DatabaseConnect()
        engine = db_connector.create_engine()
        base.metadata.create_all(engine)
    