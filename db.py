import mysql.connector.pooling
from config import Config

class Database:
    connection_pool = None

    @classmethod
    def __init__(db):
        db.connection_pool = mysql.connector.pooling.MySQLConnectionPool(
            pool_name=Config.DB_POOL_NAME,
            pool_size=int(Config.DB_POOL_SIZE),
            pool_reset_session=True,
            host=Config.DB_HOST,
            user=Config.DB_USER,
            password=Config.DB_PASSWORD,
            database=Config.DB_NAME
        )
    @classmethod
    def get_connection(db):
        if db.connection_pool is None:
            raise Exception("Database connection pool is not initialized")
        return db.connection_pool.get_connection()
    