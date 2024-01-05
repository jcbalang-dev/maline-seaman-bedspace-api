from app.utils.database import MySQLQueryExecutor

class Book:
    def __init__(self, guest_id, room_rate_id, room_bedspace_id, checkin_date, checkin_time, checkin_actual_date, checkin_actual_time, checkout_date, checkout_time, checkout_actual_date, checkout_actual_time, payment, payment_mode, payment_refno, extension_fee, extension_mode, extension_refno, status, added_by, added_date, updated_by, updated_date):
        self.guest_id = guest_id
        self.room_rate_id = room_rate_id
        self.room_bedspace_id = room_bedspace_id
        self.checkin_date = checkin_date
        self.checkin_time = checkin_time
        self.checkin_actual_date = checkin_actual_date
        self.checkin_actual_time = checkin_actual_time
        self.checkout_date = checkout_date
        self.checkout_time = checkout_time
        self.checkout_actual_date = checkout_actual_date
        self.checkout_actual_time = checkout_actual_time
        self.payment = payment
        self.payment_mode = payment_mode
        self.payment_refno = payment_refno
        self.extension_fee = extension_fee
        self.extension_mode = extension_mode
        self.extension_refno = extension_refno
        self.status = status
        self.added_by = added_by
        self.added_date = added_date
        self.updated_by = updated_by
        self.updated_date = updated_date

class BookModel:
    def __init__(self):
        self.db_exec = MySQLQueryExecutor()

    def get_all_books(self):
        self.db_exec.isFetchAll = True

        query = "SELECT * FROM book"
        
        books = self.db_exec.execute_query(query)
        
        return books

    def get_book(self, id):
        self.db_exec.isFetchAll = False
        query = "SELECT * FROM book WHERE id = %s"

        params = (id,)
        
        result = self.db_exec.execute_query(query, params)

        if result:
            book = Book(*result)  # Unpack the result tuple into a Book instance
            return book
        else:
            return None
