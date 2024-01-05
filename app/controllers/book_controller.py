from flask_restful import Resource
from app.models.book_model import BookModel
from app.views.book_view import BookView

book_model = BookModel()

class GetAllBookController(Resource):
    def get(self):
        books = book_model.get_all_books()
        if books:
            books_list = list(books)
            return BookView.render_books(books_list)
        else:
            return {'error': 'Data not found'}, 404

class GetBookIDController(Resource):
    def get(self, book_id):      
        book = book_model.get_book(book_id)
        if book:
            return BookView.render_book(book)
        else:
            return {'error': 'Book not found'}, 404
