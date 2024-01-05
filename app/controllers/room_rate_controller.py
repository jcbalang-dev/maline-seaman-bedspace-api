from flask_restful import Resource
from app.models.room_rate_model import RoomRateModel
from app.views.room_rate_view import RoomRateView

room_rate_model = RoomRateModel()

class GetAllRoomRateController(Resource):
    def get(self):
        room_rates = room_rate_model.get_all_room_rates()
        if room_rates:
            return RoomRateView.render_room_rates(room_rates)
        else:
            return {'error', 'Data not exists'}, 404
        
class GetRoomRateIDController(Resource):
        def get(self, room_rate_id):      
            room_rate = room_rate_model.get_room_rate(room_rate_id)
            if room_rate:
                return RoomRateView.render_room_rate(room_rate)
            else:
                return {'error', 'Room not found'}, 404
