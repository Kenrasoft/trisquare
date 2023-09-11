from sqlalchemy import Column, String, DateTime, Float, Integer, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from pulse.repository.database_connect import DatabaseConnect
from pulse.repository.pulsedb_base import PulseDB_Base
from datetime import datetime

Base = declarative_base()

class Global_stocks_table(Base, PulseDB_Base):
# Entity class for the DB table Global companies. 
# Manage all the operations like loading and fetching the data from the global stocks table.

    __tablename__ = 'globalstocks'
    symbol = Column(String, primary_key=True)
    company_name = Column(String)
    price = Column(Float)
    exchange = Column(String)
    exchange_short_name = Column(String)
    company_type = Column(String)


    def getBase(self):
        return Base

    def convert(self, element):
        row = Global_stocks_table(
            symbol=element["symbol"],
            company_name=element["name"],
            price=element["price"],
            exchange=element["exchange"],
            exchange_short_name=element["exchangeShortName"],
            company_type=element["type"]
        )
        return row
    

class Global_etfs_table(Base, PulseDB_Base):
# Entity class for the DB table Global etf companies. 
# Manage all the operations like loading and fetching the data from the global etf table.

    __tablename__ = 'globaletfs'
    symbol = Column(String, primary_key=True)
    company_name = Column(String)
    price = Column(Float)
    exchange = Column(String)
    exchange_short_name = Column(String)
    company_type = Column(String)


    def getBase(self):
        return Base

    def convert(self, element):
        row = Global_etfs_table(
            symbol=element["symbol"],
            company_name=element["name"],
            price=element["price"],
            exchange=element["exchange"],
            exchange_short_name=element["exchangeShortName"],
            company_type=element["type"]
        )
        return row

class Stock_prices_table(Base, PulseDB_Base):
    __tablename__ = 'stockprices'
    symbol = Column(String, primary_key=True)
    date_time = Column(DateTime, primary_key=True)  # Change the data type to DateTime
    company_name = Column(String)
    price = Column(Float)
    changes_percentage = Column(Float)
    day_change = Column(Float)
    day_low = Column(Float)
    day_high = Column(Float)
    year_high = Column(Float)
    year_low = Column(Float)
    market_cap = Column(BigInteger)
    price_avg_50 = Column(Float)
    price_avg_200 = Column(Float)
    exchange = Column(String)
    volume = Column(Integer)
    avg_volume = Column(Integer)
    open_price = Column(Float)
    previous_close = Column(Float)
    eps = Column(Float)
    pe = Column(Float)
    earnings_announcement = Column(DateTime)
    shares_outstanding = Column(BigInteger)

    def getBase(self):
        return Base

    def convert(self, element):
        row = Stock_prices_table(
                symbol=element["symbol"],
                date_time = datetime.fromtimestamp(element["timestamp"]),
                company_name=element["name"],
                price=element["price"],
                changes_percentage=element["changesPercentage"],
                day_change=element["change"],
                day_low=element["dayLow"],
                day_high=element["dayHigh"],
                year_high=element["yearHigh"],
                year_low=element["yearLow"],
                market_cap=element["marketCap"],
                price_avg_50=element["priceAvg50"],
                price_avg_200=element["priceAvg200"],
                exchange=element["exchange"],
                volume=element["volume"],
                avg_volume=element["avgVolume"],
                open_price=element["open"],
                previous_close=element["previousClose"],
                eps=element["eps"],
                pe=element["pe"],
                earnings_announcement=element["earningsAnnouncement"],
                shares_outstanding=element["sharesOutstanding"]
            )
        return row


class Historic_prices_table(Base, PulseDB_Base):
    __tablename__ = 'historic_prices'
    symbol = Column(String, primary_key=True)
    date_time = Column(DateTime, primary_key=True)
    open_price = Column(Float)
    day_high = Column(Float)
    day_low = Column(Float)
    close_price = Column(Float)
    adj_close = Column(Float)
    volume = Column(Integer)
    unadjusted_volume = Column(Integer)
    day_change = Column(Float)
    change_percent = Column(Float)
    vwap = Column(Float)
    label_name = Column(String)
    change_over_time = Column(Float)
    market_cap = Column(Float)

    def getBase(self):
        return Base

    def convert(self, element):
        row = Historic_prices_table(
                symbol=element["symbol"],
                date_time=element["date"],
                open_price=element["open"],
                day_high=element["high"],
                day_low=element["low"],
                close_price=element["close"],
                adj_close=element["adjClose"],
                volume=element["volume"],
                unadjusted_volume=element["unadjustedVolume"],
                day_change=element["change"],
                change_percent=element["changePercent"],
                vwap=element["vwap"],
                label_name=element["label"],
                change_over_time=element["changeOverTime"],
                market_cap=element["marketCap"]
            )
        return row

