from flask import Flask
from flask_cors import CORS
from pangea.routes import sectors

app = Flask(__name__)
CORS(app)  # Add this line to enable CORS for your entire Flask app.

app.register_blueprint(sectors.sectors)

if __name__ == "__main__":
    app.run(debug=True)
