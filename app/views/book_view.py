from flask import jsonify

class BookView:
    @staticmethod
    def serialize_book(book):
        return {
            'id': book.id,
            'guest_id': book.guest_id,
            'room_rate_id': book.room_rate_id,
            'checkin_date': book.checkin_date.strftime("%Y-%m-%d"),
            'checkin_time': book.checkin_time.strftime("%H:%M:%S"),
            'checkin_actual_date': book.checkin_actual_date.strftime("%Y-%m-%d"),
            'checkin_actual_time': book.checkin_actual_time.strftime("%H:%M:%S"),
            'checkout_date': book.checkout_date.strftime("%Y-%m-%d"),
            'checkout_time': book.checkout_time.strftime("%H:%M:%S"),
            'checkout_actual_date': book.checkout_actual_date.strftime("%Y-%m-%d"),
            'checkout_actual_time': book.checkout_actual_time.strftime("%H:%M:%S"),
            'payment': float(book.payment),
            'payment_mode': book.payment_mode,
            'payment_refno': book.payment_refno,
            'extension_fee': float(book.extension_fee),
            'extension_mode': book.extension_mode,
            'extension_refno': book.extension_refno,
            'status': book.status,
            'added_by': book.added_by,
            'checkin_date': book.checkin_date.strftime("%Y-%m-%d %H:%M:%S"),
            'updated_by': book.updated_by,
            'updated_date': book.updated_date.strftime("%Y-%m-%d %H:%M:%S"),
        }

    @staticmethod
    def render_book(book):
        return jsonify(BookView.serialize_book(book))

    @staticmethod
    def render_books(books):
        result = []
        for book in books:
            book_dict = {
                'id' : book[0],
                'building_id' : book[1],
                'room_rate_id' : book[2],
                'room_bedspace_id' : book[3],
                'checkin_date' : book[4].strftime("%Y-%m-%d"),
                'checkin_time' : book[5].strftime("%H:%M:%S"),
                'checkin_actual_date' : book[6].strftime("%Y-%m-%d"),
                'checkin_actual_time' : book[7].strftime("%H:%M:%S"),
                'checkout_date' : book[8].strftime("%Y-%m-%d"),
                'checkout_time' : book[9].strftime("%H:%M:%S"),
                'checkout_actual_date' : book[10].strftime("%Y-%m-%d"),
                'checkout_actual_time' : book[11].strftime("%H:%M:%S"),
                'payment' : float(book[12]),
                'payment_mode' : book[13],
                'payment_refno' : book[14],
                'extension_fee' : float(book[15]),
                'extension_mode' : book[16],
                'extension_refno' : book[17],
                'status' : book[18],
                'added_by' : book[19],
                'added_date' : book[20],
                'updated_by' : book[21],
                'updated_date' : book[22],
            }
            result.append(book_dict)

        return {'books': result}
