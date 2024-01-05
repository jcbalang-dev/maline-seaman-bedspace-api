from app.utils.database import MySQLQueryExecutor

class Guest:
    def __init__(self, id, last_name, first_name, middle_name, suffix, passport_id, drivers_license_id, umid_id, sss_id, prc_id, status):
        self.id = id
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.suffix = suffix
        self.passport_id = passport_id
        self.drivers_license_id = drivers_license_id
        self.umid_id = umid_id
        self.sss_id = sss_id
        self.prc_id = prc_id
        self.status = status

class GuestModel:
    def __init__(self):
        self.db_exec = MySQLQueryExecutor()

    def get_all_guest(self):
        self.db_exec.isFetchAll = True

        query = """
            SELECT 
                id , 
                last_name , 
                first_name , 
                middle_name , 
                suffix , 
                passport_id , 
                drivers_license_id , 
                umid_id , 
                sss_id , 
                prc_id , 
                status 
            FROM 
                guest
        """

        guests = self.db_exec.execute_query(query)

        return guests

    def get_guest(self, guest_id):
        self.db_exec.isFetchAll = False

        query = """
            SELECT 
                id , 
                last_name , 
                first_name , 
                middle_name , 
                suffix , 
                passport_id , 
                drivers_license_id , 
                umid_id , 
                sss_id , 
                prc_id , 
                status 
            FROM 
                guest
            WHERE
                id = %s
        """
        
        params = (guest_id,)

        result = self.db_exec.execute_query(query, params)
        
        if result:
            id, last_name, first_name, middle_name, suffix, passport_id, drivers_license_id, umid_id, sss_id, prc_id, status = result
            
            return Guest(
                id = id , 
                last_name = last_name , 
                first_name = first_name , 
                middle_name = middle_name , 
                suffix = suffix , 
                passport_id = passport_id , 
                drivers_license_id = drivers_license_id , 
                umid_id = umid_id , 
                sss_id = sss_id , 
                prc_id = prc_id , 
                status = status 
            )
        else:
            return None
            