"""
The purpose of this sectors.py file is to create routes using FlaskAPI (to query the data from the data base and to show it in the UI).

This module imports the Queries file from pulse.repository.queries, All the methods in this file make use of the the functionalities of queries.py file.
"""

from flask import Blueprint, jsonify, request
from pulse.repository.queries import Queries
# The sectors.py here is used to create the routes using FlaskAPI.
sectors = Blueprint("sectors", __name__)

# This route gets the method in Queries class with query of getting sectors in sp500 
# and shows in /sectors route.
@sectors.route('/sectors', methods=['GET'])
def get_sectors():
    """
    This route gets the method in Queries class with query of getting sectors in sp500 and shows in /sectors route.
    """

    query = Queries()
    return jsonify(query.get_sectors())

# This route gets the method in Queries class with query of getting subsectorssectors
#  for perticular sector in sp500 and shows in /sectors/subsectors route.
@sectors.route('/sectors/subsectors', methods=['GET'])
def get_sectors_subsectors():
    """
    This route gets the method in Queries class with query of getting subsectors for particular sector in sp500 and shows in /sectors/subsectors route.
    """

    query = Queries()
    selected_sector = request.args.get('sector')  
    subsectors = query.get_sectors_subsectors(selected_sector)
    return jsonify(subsectors)

# This route gets the method in Queries class with query of getting marketcap
# for perticular sector in sp500 and shows in /sectors/<string:selected_sector>/marketcap.
@sectors.route('/sectors/<string:selected_sector>/marketcap', methods=['GET'])
def get_sector_marketcap(selected_sector):
    """
    This route gets the method in Queries class with query of getting marketcap for perticular sector in sp500 and shows in /sectors/<string:selected_sector>/marketcap.
    """

    query = Queries()
    market_cap = query.get_sector_marketcap(selected_sector)
    return jsonify(market_cap)


# Add a new route for retrieving market cap data for all sectors
@sectors.route('/sectors/marketcap', methods=['GET'])
def get_all_sectors_marketcaps():
    """
    Adding a new route for retrieving market cap data for all sectors.
    """

    query = Queries()
    # Call the method to fetch market cap data for all sectors
    market_caps = query.get_all_sectors_marketcap()
    return jsonify(market_caps)
    
# Add a new route for retrieving periodic market cap data for all sectors
@sectors.route('/sectors/periodic_marketcap_data', methods=['GET'])
def get_periodic_marketcap_data():
    """
    Adding a new route for retrieving periodic market cap data for all sectors.

    Time periods - 1 day, 1 week, 1 month, 3 months, 6 months, 9 months, 1 year.

    This method calls get_periodic_marketcap_for_sectors() from pulse.repository.queries
    """

    query = Queries()
    # Call the method to fetch market cap data for all sectors
    periodic_market_caps = query.get_periodic_marketcap_for_sectors()
    return jsonify(periodic_market_caps)