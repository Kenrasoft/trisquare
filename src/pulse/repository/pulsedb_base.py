from pulse.repository.database_connect import DatabaseConnect
from sqlalchemy.exc import IntegrityError

class PulseDB_Base():

    base = None
    def convert(self, element):
        pass

    # def expand_data(row, *extra_data):
    #     pass

    def load_data(self, data): 
        db_connector = DatabaseConnect()
        session = db_connector.connect_db()
        with session() as s:
            for element in data:
                row = self.convert(element)
                # self.expand_data(row, data)
                try:
                    s.merge(row)
                    s.commit()
                except IntegrityError as e:
                    s.rollback()  # Roll back the transaction
            
    
    def create_table(self, base):
        db_connector = DatabaseConnect()
        engine = db_connector.create_engine()
        base.metadata.create_all(engine)
    