from app.utils.database import MySQLQueryExecutor

class RoomRate:
    def __init__(self, id, building_id, number, code, tag, slug, description, price, status, added_by, added_date, updated_by, updated_date):
        self.id = id
        self.building_id = building_id
        self.number = number
        self.code = code
        self.tag = tag
        self.slug = slug
        self.description = description
        self.price = price
        self.status = status
        self.added_by = added_by
        self.added_date = added_date
        self.updated_by = updated_by
        self.updated_date = updated_date

class RoomRateModel:
    def __init__(self):
        self.db_exec = MySQLQueryExecutor()

    def get_all_room_rates(self):
        self.db_exec.isFetchAll = True

        query = "SELECT * FROM room_rate"
        
        room_rates = self.db_exec.execute_query(query)
        
        return room_rates

    def get_room_rate(self, id):
        self.db_exec.isFetchAll = False
        query = "SELECT * FROM room_rate WHERE id = %s"

        params = (id,)
        
        result = self.db_exec.execute_query(query, params)

        if result:
            id, building_id, number, code, tag, slug, description, price, status, added_by, added_date, updated_by, updated_date = result

            return RoomRate(
                id = id,
                building_id = building_id,
                number = number,
                code = code,
                tag = tag,
                slug = slug,
                description = description,
                price = price,
                status = status,
                added_by = added_by,
                added_date = added_date,
                updated_by = updated_by,
                updated_date = updated_date,
            )
        else:
            return None
