from flask_restful import Resource
from app.models.room_bedspace_model import RoomBedSpaceModel
from app.views.room_bedspace_view import RoomBedSpaceView

room_bedspace_model = RoomBedSpaceModel()

class GetAllRoomBedSpaceController(Resource):
    def get(self):
        room_bedspaces = room_bedspace_model.get_all_room_bedspaces()
        if room_bedspaces:
            return RoomBedSpaceView.render_room_bedspaces(room_bedspaces)
        else:
            return {'error', 'Data not exists'}, 404
        
class GetRoomBedSpaceIDController(Resource):
        def get(self, room_bedspace_id):      
            room_bedspace = room_bedspace_model.get_room_bedspace(room_bedspace_id)
            if room_bedspace:
                return RoomBedSpaceView.render_room_bedspace(room_bedspace)
            else:
                return {'error', 'Room not found'}, 404
