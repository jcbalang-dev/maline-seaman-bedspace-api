from flask_restful import Resource
from app.models.room_model import RoomModel
from app.views.room_view import RoomView

room_model = RoomModel()

class GetAllRoomController(Resource):
    def get(self):
        rooms = room_model.get_all()
        if rooms:
            return RoomView.render_rooms(rooms)
        else:
            return {'error', 'Data not exists'}, 404
        
class GetRoomIDController(Resource):
        def get(self, room_id):      
            room = room_model.get(room_id)
            if room:
                return RoomView.render_room(room)
            else:
                return {'error', 'Room not found'}, 404
