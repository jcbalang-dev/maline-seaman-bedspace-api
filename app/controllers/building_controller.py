from flask_restful import Resource
from app.models.building_model import BuildingModel
from app.views.building_view import BuildingView

building_model = BuildingModel()

class GetAllBuildingController(Resource):
    def get(self):
        buildings = building_model.get_all()
        if buildings:
            return BuildingView.render_buildings(buildings)
        else:
            return {'error', 'Data not exists'}, 404
        
class GetBuildingIDController(Resource):
    def get(self, building_id):      
        building = building_model.get(building_id)
        if building:
            return BuildingView.render_building(building)
        else:
            return {'error', 'Building not found'}, 404
