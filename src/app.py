"""
The purpose of this app.py file is to handle the routes.

Run this app.py to get acces for api routes in browser. http://127.0.0.1:5000/{routes}

This module imports Flask, CORS, sectors file (from pangea.routes)
"""

from flask import Flask
from flask_cors import CORS
from pangea.routes import sectors

app = Flask(__name__)
CORS(app)


app.register_blueprint(sectors.sectors)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)  # Change the port to your desired value
