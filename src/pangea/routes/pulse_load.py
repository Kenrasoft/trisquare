from flask import Blueprint, jsonify, request
from pulse.integration.fmpapi_to_db import FmpApiToDatabase

pulse_load = Blueprint('pulse_load',__name__)

query_string_to_function_mapping = {
    "indexCompanies": FmpApiToDatabase.load_index_companies,
    "globalStocks": FmpApiToDatabase.load_global_stocks,
    "historicalPrices": FmpApiToDatabase.load_historical_prices,
    "dailyPrices": FmpApiToDatabase.load_daily_prices,
    "compAnalysis":FmpApiToDatabase.load_company_analysis
}

@pulse_load.route('/pulse/load', methods=['GET'])
def get_load_pulse_data():
    # Reading query parameter 'data' from request
    selected_data= request.args.get('data')    
    function = query_string_to_function_mapping.get(selected_data)
    try:
        if function:
            function()           
            response = jsonify({"message": f"Loaded {selected_data} data successfully"}),200
        else:
            response=jsonify({"error": "Bad Request ---Invalid data"}),400           
    except Exception as e:
        response = jsonify({"error": "Internal Server Error","Exception": str(e)}),500
    return response


