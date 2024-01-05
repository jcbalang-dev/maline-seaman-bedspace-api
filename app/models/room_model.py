from app.utils.database import MySQLQueryExecutor
from abc import ABC
from typing import List

class Room(ABC):
    def __init__(self, id, building_id, number, code, tag, slug, rate, bed_capacity, availability, description, added_by, added_date, updated_by, updated_date):
        self.id = id
        self.building_id = building_id
        self.number = number
        self.code = code
        self.tag = tag
        self.slug = slug
        self.rate = rate
        self.bed_capacity = bed_capacity
        self.availability = availability
        self.description = description
        self.added_by = added_by
        self.added_date = added_date
        self.updated_by = updated_by
        self.updated_date = updated_date

class RoomModel:
    def __init__(self):
        self.db_exec = MySQLQueryExecutor()

    def _create_object(self, row) -> Room:
        id, building_id, number, code, tag, slug, rate, bed_capacity, availability, description, added_by, added_date, updated_by, updated_date = row
        return Room(
            id = id ,
            building_id = building_id ,
            number = number ,
            code = code ,
            tag = tag ,
            slug = slug ,
            rate = rate ,
            bed_capacity = bed_capacity ,
            availability = availability ,
            description = description ,
            added_by = added_by ,
            added_date = added_date ,
            updated_by = updated_by ,
            updated_date= updated_date
        )
    
    def _create_objects(self, rows) -> List[Room]:
        return [self._create_object(row) for row in rows]
    
    def get_all(self):
        self.db_exec.isFetchAll = True
        query = """
            SELECT 
                id , 
                building_id , 
                number , 
                code , 
                tag , 
                slug , 
                rate , 
                bed_capacity , 
                availability , 
                description , 
                added_by , 
                added_date , 
                updated_by , 
                updated_date 
            FROM 
                room
            """
        rooms = self.db_exec.execute_query(query)
        return self._create_objects(rooms)

    def get(self, id):
        self.db_exec.isFetchAll = False
        query = """
             SELECT 
                id , 
                building_id , 
                number , 
                code , 
                tag , 
                slug , 
                rate , 
                bed_capacity , 
                availability , 
                description , 
                added_by , 
                added_date , 
                updated_by , 
                updated_date 
            FROM 
                room       
            WHERE 
                id = %s
            """
        params = (id,)
        result = self.db_exec.execute_query(query, params)
        if result:
            return self._create_object(result)
        else:
            return None
