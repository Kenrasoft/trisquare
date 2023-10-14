"""
The purpose of this database_connect.py file is to instantiate database connections and sessions.

This module imports the config file (which stores details to access the data base) from core.configuration.config.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.configuration.config_singleton import config_singleton_a


class DatabaseConnect:
    """
    The centralized class for the database connections and sessions.
    """

    def __init__(self) -> None:
        self.session = None

    def create_engine(self):
        """
        Creates the database engine using - username, password, hostname, port number and the database name obtained from the config file.
        
        :return: The database connection (engine) established using create_engine().
        """
        
        config = config_singleton_a()
        db_config = config.load_config()["database"]
        DATABASE_URL = f"postgresql://{db_config['username']}:{db_config['password']}@host.docker.internal:{db_config['port']}/{db_config['database']}"
        engine = create_engine(DATABASE_URL)
        return engine

    def connect_db(self):
        """
        Establishes the data base connection using the details - username, password, hostname, port number and the database name obtained from the config file.
        
        :return: The database session created using create_engine() and sessionmaker().
        """

        engine = self.create_engine()
        session = sessionmaker(bind=engine)
        return session

    
