from app.utils.database import MySQLQueryExecutor
from abc import ABC
from typing import List

class User(ABC):
    def __init__(self, id, last_name, first_name, middle_name, user_id, email, status):
        self.id = id
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.user_id = user_id
        self.email = email
        self.status = status

class UserModel:
    def __init__(self):
        self.db_exec = MySQLQueryExecutor()

    def _create_object(self, row) -> User:
        id, last_name, first_name, middle_name, user_id, email, status = row
        return User(
            id = id ,
            last_name = last_name ,
            first_name = first_name ,
            middle_name = middle_name ,
            user_id = user_id ,
            email = email ,
            status = status
        )

    def _create_objects(self, rows) -> List[User]:
        return [self._create_object(row) for row in rows]

    def get_all(self):
        self.db_exec.isFetchAll = True
        query = """
            SELECT 
                id , 
                last_name , 
                first_name , 
                middle_name , 
                user_id , 
                email , 
                status 
            FROM 
                user
        """
        users = self.db_exec.execute_query(query)
        return self._create_objects(users) 

    def get(self, id):
        self.db_exec.isFetchAll = False
        query = """
            SELECT 
                id , 
                last_name , 
                first_name , 
                middle_name , 
                user_id ,
                email , 
                status 
            FROM 
                user 
            WHERE 
                id = %s 
        """
        params = (id, )
        result = self.db_exec.execute_query(query, params)
        if result:
           return self._create_object(result)
        else:
            return None

    def auth_login(self, user_id, password):
        self.db_exec.isFetchAll = False
        query = """
            SELECT 
                id , 
                last_name , 
                first_name , 
                middle_name , 
                user_id ,
                email , 
                status 
            FROM 
                user 
            WHERE 
                user_id = %s 
                AND password = %s
        """
        params = (user_id, password, )
        result = self.db_exec.execute_query(query, params)
        if result:
            return self._create_object(result)
        else:
            return None
        