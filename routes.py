from flask_restful import Api
from app.controllers.user_controller import GetAllUserController, GetUserIdController, UserAuthController
from app.controllers.guest_controller import GetAllGuestController, GetGuestIDController
from app.controllers.room_bedspace_controller import GetAllRoomBedSpaceController, GetRoomBedSpaceIDController
from app.controllers.room_controller import GetAllRoomController, GetRoomIDController
from app.controllers.building_controller import GetAllBuildingController, GetBuildingIDController
from app.controllers.room_rate_controller import GetAllRoomRateController, GetRoomRateIDController
from app.controllers.book_controller import GetAllBookController, GetBookIDController

class Routes:
    def __init__(self, api):
        self.api = api

    def setup_routes(self):
        # routes list
        self.api.add_resource(UserAuthController, "/login")
        self.api.add_resource(GetAllUserController, "/users")
        self.api.add_resource(GetUserIdController, "/user/<string:id>")
        self.api.add_resource(GetAllGuestController, "/guests")
        self.api.add_resource(GetGuestIDController, "/guest/<string:guest_id>")
        self.api.add_resource(GetAllRoomBedSpaceController, "/room_bedspaces")
        self.api.add_resource(GetRoomBedSpaceIDController, "/room_bedspace/<string:room_bedspace_id>")
        self.api.add_resource(GetAllRoomController, "/rooms")
        self.api.add_resource(GetRoomIDController, "/room/<string:room_id>")
        self.api.add_resource(GetAllBuildingController, "/buildings")
        self.api.add_resource(GetBuildingIDController, "/building/<string:building_id>")
        self.api.add_resource(GetAllRoomRateController, "/room_rates")
        self.api.add_resource(GetRoomRateIDController, "/room_rate/<string:room_rate_id>")
        self.api.add_resource(GetAllBookController, "/books")
        self.api.add_resource(GetBookIDController, "/book/<string:book_id>")
