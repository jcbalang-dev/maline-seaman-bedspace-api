from flask_restful import Resource, request
from app.models.guest_model import GuestModel
from app.views.guest_view import GuestView

guest_model = GuestModel()

class GetAllGuestController(Resource):
    def get(self):
        guests = guest_model.get_all_guest()
        if guests:
            return GuestView.render_guests(guests)
        else:
            return {'error', 'Data not exists'}, 404

class GetGuestIDController(Resource):
    def get(self, guest_id):        
        guest = guest_model.get_guest(guest_id)
        if guest:
            return GuestView.render_guest(guest)
        else:
            return {'error', 'Guest not found'}, 404
        