from pulse.repository.database_connect import DatabaseConnect
from pulse.repository.index_companies_repo import SP500_table
from pulse.repository.stock_prices_repo import Daily_prices_table
from pulse.repository.stock_prices_repo import Historical_prices_table
from sqlalchemy import func
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta

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
                sectors_and_subsectors = (
                    session.query(SP500_table.sector, SP500_table.subsector)
                    .filter(SP500_table.sector == selected_sector)
                    .distinct()
                    .all()
                )
            else:
                # Query all subsectors
                sectors_and_subsectors = (
                    session.query(SP500_table.sector, SP500_table.subsector)
                    .distinct()
                    .all()
                )
        # Convert the data to a list of dictionaries
        data = [
            {"sector": sector, "subSector": subsector}
            for sector, subsector in sectors_and_subsectors
        ]
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
            # Query the SP500_table to get all symbols in the selected sector
            sector_companies = (
                session.query(SP500_table.symbol)
                .filter(SP500_table.sector == selected_sector)
                .all()
            )
            symbols = [company[0] for company in sector_companies]

            # Calculate the total market cap for companies in the selected sector
            total_marketcap = (
                session.query(func.sum(Daily_prices_table.market_cap))
                .filter(Daily_prices_table.symbol.in_(symbols))
                .scalar()
            )
            formatted_market_cap = f"${total_marketcap:,}"

        return {"sector": selected_sector, "total_marketcap": formatted_market_cap}

    def get_all_sectors_marketcap(self):
        db_connector = DatabaseConnect()
        session = db_connector.connect_db()

        with session() as session:
            # Query all sectors in SP500
            sectors = session.query(SP500_table.sector).distinct().all()
            sectors = [sector[0] for sector in sectors]

            sector_marketcaps = {}

            for sector in sectors:
                # Query the SP500_table to get all symbols in the current sector
                sector_companies = (
                    session.query(SP500_table.symbol)
                    .filter(SP500_table.sector == sector)
                    .all()
                )
                symbols = [company[0] for company in sector_companies]

                # Calculate the total market cap for companies in the current sector
                total_marketcap = (
                    session.query(func.sum(Daily_prices_table.market_cap))
                    .filter(Daily_prices_table.symbol.in_(symbols))
                    .scalar()
                )

                # Format the market cap for the current sector
                formatted_market_cap = f"${total_marketcap:,}"

                # Store the market cap for the sector in the dictionary
                sector_marketcaps[sector] = formatted_market_cap

        return sector_marketcaps

    def get_previous_working_date_with_market_cap(
        self, session, date_to_check, symbols
    ):
        while True:
            # Check if the date has a non-null market cap
            market_cap = (
                session.query(func.sum(Historical_prices_table.market_cap))
                .filter(
                    Historical_prices_table.symbol.in_(symbols),
                    func.date(Historical_prices_table.date_time) == date_to_check,
                )
                .scalar()
            )
            if market_cap is not None:
                return date_to_check  # Found a non-null market cap for this date

            # If market_cap is still None, move to the previous date
            date_to_check -= timedelta(days=1)

    def get_periodic_marketcap_for_sectors(self):
        db_connector = DatabaseConnect()
        session = db_connector.connect_db()

        # Get today's date as a datetime object

        with session() as session:
            # Query all sectors in SP500
            sectors = session.query(SP500_table.sector).distinct().all()
            sectors = [sector[0] for sector in sectors]
            periodic_marketcap_for_sectors = {}
            sector_periodic_marketcap_data = []
            for sector in sectors:
                # Query the SP500_table to get all symbols in the current sector
                sector_companies = (
                    session.query(SP500_table.symbol)
                    .filter(SP500_table.sector == sector)
                    .all()
                )
                symbols = [company[0] for company in sector_companies]

                today = date.today()
                today = self.get_previous_working_date_with_market_cap(
                    session, today, symbols
                )

                # Calculate the previous date by subtracting one day
                previous_date = today - timedelta(days=1)
                previous_working_date = self.get_previous_working_date_with_market_cap(
                    session, previous_date, symbols
                )

                # Calculate the one week back date by subtracting 7 days
                oneweek_back_Date = today - timedelta(days=7)
                oneweek_back_working_date = (
                    self.get_previous_working_date_with_market_cap(
                        session, oneweek_back_Date, symbols
                    )
                )

                # Calculate the date one month back
                one_month_back = today - relativedelta(months=1)
                one_month_back_working_date = (
                    self.get_previous_working_date_with_market_cap(
                        session, one_month_back, symbols
                    )
                )

                # Calculate the date three months back
                three_months_back = today - relativedelta(months=3)
                three_months_back_working_date = (
                    self.get_previous_working_date_with_market_cap(
                        session, three_months_back, symbols
                    )
                )

                # Calculate the date six months back
                six_months_back = today - relativedelta(months=6)
                six_months_back_working_date = (
                    self.get_previous_working_date_with_market_cap(
                        session, six_months_back, symbols
                    )
                )

                # Calculate the date one year back, considering leap years
                one_year_back = today - relativedelta(years=1)
                one_year_back_working_date = (
                    self.get_previous_working_date_with_market_cap(
                        session, one_year_back, symbols
                    )
                )

                # Calculate the total market cap for companies in the current sector
                current_marketcap = (
                    session.query(func.sum(Historical_prices_table.market_cap))
                    .filter(
                        Historical_prices_table.symbol.in_(symbols),
                        func.date(Historical_prices_table.date_time) == today,
                    )
                    .scalar()
                )

                previous_marketcap = (
                    session.query(func.sum(Historical_prices_table.market_cap))
                    .filter(
                        Historical_prices_table.symbol.in_(symbols),
                        func.date(Historical_prices_table.date_time)
                        == previous_working_date,
                    )
                    .scalar()
                )

                oneweek_back_marketcap = (
                    session.query(func.sum(Historical_prices_table.market_cap))
                    .filter(
                        Historical_prices_table.symbol.in_(symbols),
                        func.date(Historical_prices_table.date_time)
                        == oneweek_back_working_date,
                    )
                    .scalar()
                )

                onemonth_back_marketcap = (
                    session.query(func.sum(Historical_prices_table.market_cap))
                    .filter(
                        Historical_prices_table.symbol.in_(symbols),
                        func.date(Historical_prices_table.date_time)
                        == one_month_back_working_date,
                    )
                    .scalar()
                )

                threemonth_back_marketcap = (
                    session.query(func.sum(Historical_prices_table.market_cap))
                    .filter(
                        Historical_prices_table.symbol.in_(symbols),
                        func.date(Historical_prices_table.date_time)
                        == three_months_back_working_date,
                    )
                    .scalar()
                )

                sixmonth_back_marketcap = (
                    session.query(func.sum(Historical_prices_table.market_cap))
                    .filter(
                        Historical_prices_table.symbol.in_(symbols),
                        func.date(Historical_prices_table.date_time)
                        == six_months_back_working_date,
                    )
                    .scalar()
                )

                oneyear_back_marketcap = (
                    session.query(func.sum(Historical_prices_table.market_cap))
                    .filter(
                        Historical_prices_table.symbol.in_(symbols),
                        func.date(Historical_prices_table.date_time)
                        == one_year_back_working_date,
                    )
                    .scalar()
                )

                sector_periodic_marketcap_data.append(
                    (
                        sector,
                        current_marketcap,
                        previous_marketcap,
                        oneweek_back_marketcap,
                        onemonth_back_marketcap,
                        threemonth_back_marketcap,
                        sixmonth_back_marketcap,
                        oneyear_back_marketcap,
                    )
                )

                # Store the market cap for the sector in the dictionary
                # periodic_marketcap_for_sectors[sector] = formatted_market_cap

                periodic_marketcap_for_sectors = [
                    {
                        "sector": sector,
                        "current_marketcap": current_marketcap,
                        "previous_marketcap": previous_marketcap,
                        "oneweek_back": oneweek_back_marketcap,
                        "onemonth_back": onemonth_back_marketcap,
                        "threemonths_back": threemonth_back_marketcap,
                        "sixmonths_back": sixmonth_back_marketcap,
                        "oneyear_back": oneyear_back_marketcap,
                    }
                    for sector, current_marketcap, previous_marketcap, oneweek_back_marketcap, onemonth_back_marketcap, threemonth_back_marketcap, sixmonth_back_marketcap, oneyear_back_marketcap in sector_periodic_marketcap_data
                ]

            return periodic_marketcap_for_sectors
        

    def get_market_cap_data(self, table_name):
        db_connector = DatabaseConnect()
        session = db_connector.connect_db()

        with session() as session:
            # Query the database for sectors
            results = session.query(
                func.date(table_name.date_time).label('date_on'),
                SP500_table.sector,
                SP500_table.subsector,
                func.sum(table_name.market_cap).label('market_cap')
                ).join(
                table_name,
                SP500_table.symbol == table_name.symbol
                ).group_by(
                SP500_table.subsector, SP500_table.sector, func.date(table_name.date_time)
                ).order_by(
                SP500_table.subsector, SP500_table.sector, func.date(table_name.date_time)
                ).all()
            
        # Convert the results into a list of dictionaries
        data = [
            {"date_on": date_on, "sector": sector, "subsector": subsector, "market_cap": market_cap }
            for date_on, sector, subsector, market_cap in results
        ]
        
        return data
    
    
