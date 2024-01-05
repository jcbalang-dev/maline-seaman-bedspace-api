from app.utils.database import MySQLQueryExecutor

class RoomBedspace:
    def __init__(self, id, room_id, number, code, tag, slug, availability, description, added_by, added_date, updated_by, updated_date):
        self.id = id
        self.room_id = room_id
        self.number = number
        self.code = code
        self.tag = tag
        self.slug = slug
        self.availability = availability
        self.description = description
        self.added_by = added_by
        self.added_date = added_date
        self.updated_by = updated_by
        self.updated_date = updated_date

class RoomBedSpaceModel:
    def __init__(self):
        self.db_exec = MySQLQueryExecutor()

    def get_all_room_bedspaces(self):
        self.db_exec.isFetchAll = True

        query = "SELECT * FROM room_bedspace"
        
        room_bedspaces = self.db_exec.execute_query(query)
        
        return room_bedspaces

    def get_room_bedspace(self, id):
        self.db_exec.isFetchAll = False
        query = "SELECT * FROM room_bedspace WHERE id = %s"

        params = (id,)
        
        result = self.db_exec.execute_query(query, params)

        if result:
            id, room_id, number, code, tag, slug, availability, description, added_by, added_date, updated_by, updated_date = result

            return RoomBedspace(
                id = id,
                room_id = room_id,
                number = number,
                code = code,
                tag = tag,
                slug = slug,
                availability = availability,
                description = description,
                added_by = added_by,
                added_date = added_date,
                updated_by = updated_by,
                updated_date = updated_date,
            )
        else:
            return None
