from pulse.repository.database_connect import DatabaseConnect
from pulse.repository.index_companies_repo import SP500_table
from pulse.repository.stock_prices_repo import Historical_prices_table
from sqlalchemy import func
import json

# This class has all the different queries of different tables that can be used.
class Queries:
    def get_sectors(self):
        db_connector = DatabaseConnect()
        session = db_connector.connect_db()
        with session() as session:
            # Query the database for sectors
            sectors = session.query(SP500_table.sector).distinct().all()
            # Convert the data to a list of dictionaries
            data = [{"sector": sector} for sector, in sectors]
            return data
        
    def get_sectors_subsectors(self, selected_sector=None):
        db_connector = DatabaseConnect()
        session = db_connector.connect_db()
        with session() as session:
            if selected_sector:
                # Query the database for subsectors based on the selected sector
                sectors_and_subsectors = session.query(SP500_table.sector, SP500_table.subsector).filter(SP500_table.sector == selected_sector).distinct().all()
            else:
                # Query all subsectors
                sectors_and_subsectors = session.query(SP500_table.sector, SP500_table.subsector).distinct().all()
        # Convert the data to a list of dictionaries
        data = [{"sector": sector, "subSector": subsector} for sector, subsector in sectors_and_subsectors]
        return data
        
    def get_symbols(self):
        db_connector = DatabaseConnect()
        session = db_connector.connect_db()
        with session() as session:
            symbols_query = session.query(SP500_table.symbol).all()
            symbols = [symbol[0] for symbol in symbols_query]
            return symbols
        
    def get_sector_marketcap(self, selected_sector=None):
        db_connector = DatabaseConnect()
        session = db_connector.connect_db()
        with session() as session:
            sector_companies = session.query(SP500_table.symbol).filter(SP500_table.sector == selected_sector).all()
            symbols = [company[0] for company in sector_companies]
            
            date_query = session.query(Historical_prices_table.date_time).distinct().all()
            dates = [ d for d, in date_query]
            
            values=[]
            
            for d in dates:
                total_marketcap = (
                    session.query(func.sum(Historical_prices_table.market_cap))
                    .filter(Historical_prices_table.symbol.in_(symbols))
                    .where(Historical_prices_table.date_time == d)
                    .scalar()
                    )
                total_volume = (
                    session.query(func.sum(Historical_prices_table.volume))
                    .filter(Historical_prices_table.symbol.in_(symbols))
                    .where(Historical_prices_table.date_time == d)
                    .scalar()
                    )

                values.append({ "date": d.strftime('%Y-%m-%d') , "volume": total_volume ,"marketcap" : total_marketcap })

            return values
        
    def get_all_sector_marketcap(self):
        db_connector = DatabaseConnect()
        session = db_connector.connect_db()
        with session() as session:
            sectors = session.query(SP500_table.sector).distinct().all()
            data = [sector for sector, in sectors]
            data_for_sectors = []
            for i in data:
                
                values = Queries().get_sector_marketcap(i)
                output = {"sector":i, "historical":values}
                data_for_sectors.append(output)

            output_file = {"historicalSectors":data_for_sectors}
            
            file_path = './pulse/repository/sectors_data.json'  

            with open(file_path, 'w') as file:
                json.dump(output_file, file, indent=4)
            
            return
            


