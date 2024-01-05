from flask import Flask
from flask_restful import Api
from dotenv import dotenv_values
from config import Config
from db import Database
from routes import Routes
from flask_cors import CORS

# Initialize the Flask app
app = Flask(__name__)

# Load environment variables from .env
env = dotenv_values()

# Disable JSON sorting alphabetically globally
app.json.sort_keys = Config.FLASK_JSON_SORT_KEYS

# server port
api_port = Config.API_PORT

# Database configuration
db = Database

# Initialize the Flask-RESTful API
api = Api(app)

# Enable CORS for your app
CORS(app, resources={r"/*": {"origins": Config.CORS_ALLOWED_ORIGINS}})

# Setup routes
routes = Routes(api)
routes.setup_routes()

# Application run
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=api_port, debug=True)
