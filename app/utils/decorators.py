import mysql.connector
from mysql.connector import errorcode
from functools import wraps

class ReconnectOnFailure:
    def __init__(self, max_retries=3):
        self.max_retries = max_retries

    def __call__(self, func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            retries = 0
            while retries < self.max_retries:
                try:
                    connection = self.db.get_connection()
                    result = func(self, connection, *args, **kwargs)
                    connection.close()
                    return result
                except mysql.connector.Error as err:
                    if err.errno == errorcode.CR_SERVER_GONE_ERROR:
                        # handles reconnection 
                        retries += 1
                    else:
                        raise err
            raise Exception(f"Max retries ({self.max_retries} reached. Unable to execute query.)")
        return wrapper
