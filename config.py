from dotenv import dotenv_values
import os

env = dotenv_values()

class Config:
    """ Environment variables """
    # MySQL connection
    DB_HOST = env.get('DB_HOST', 'localhost')
    DB_USER = env.get('DB_USER')
    DB_PASSWORD = env.get('DB_PASSWORD')
    DB_NAME = env.get('DB_NAME')
    DB_POOL_NAME = env.get('DB_POOL_NAME', 'dls_api')
    DB_POOL_SIZE = env.get('DB_POOL_SIZE', 5)
    DB_RECONNECT_MAX_RETRY = env.get('DB_RECONNECT_MAX_RETRY', 3)

    # server port
    API_PORT = int(env.get('API_PORT', 5000))

    # flask app json sort key flag 
    FLASK_JSON_SORT_KEYS = bool(env.get('FLASK_JSON_SORT_KEYS', False))
    
    #CORS origins
    CORS_ALLOWED_ORIGINS = os.environ.get("CORS_ALLOWED_ORIGINS", "*")
