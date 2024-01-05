from app.utils.database import MySQLQueryExecutor
from abc import ABC
from typing import List

class Building(ABC):
    def __init__(self, id, code, tag, slug, name, address, description, added_by, added_date, updated_by, updated_date):
        self.id = id
        self.code = code
        self.tag = tag
        self.slug = slug
        self.name = name
        self.address = address
        self.description = description
        self.added_by = added_by
        self.added_date = added_date
        self.updated_by = updated_by
        self.updated_date = updated_date

class BuildingModel:
    def __init__(self):
        self.db_exec = MySQLQueryExecutor()

    def _create_object(self, row) -> Building:
        id, code, tag, slug, name, address, description, added_by, added_date, updated_by, updated_date = row
        return Building(
            id = id ,
            code = code ,
            tag = tag ,
            slug = slug ,
            name = name ,
            address = address ,
            description = description ,
            added_by = added_by ,
            added_date = added_date ,
            updated_by = updated_by ,
            updated_date = updated_date
        )
        
    def _create_objects(self, rows) -> List[Building]:
        return [self._create_object(row) for row in rows]

    def get_all(self):
        self.db_exec.isFetchAll = True
        query = """
            SELECT 
                id , 
                code , 
                tag , 
                slug , 
                name , 
                address , 
                description , 
                added_by , 
                added_date , 
                updated_by , 
                updated_date 
            FROM 
                building
            """
        buildings = self.db_exec.execute_query(query)
        return self._create_objects(buildings)

    def get(self, id):
        self.db_exec.isFetchAll = False
        query = """
            SELECT 
                id , 
                code , 
                tag , 
                slug , 
                name , 
                address , 
                description , 
                added_by , 
                added_date , 
                updated_by , 
                updated_date 
            FROM 
                building
            WHERE 
                id = %s
            """
        params = (id,)
        result = self.db_exec.execute_query(query, params)
        if result:
            return self._create_object(result)
        else:
            return None
