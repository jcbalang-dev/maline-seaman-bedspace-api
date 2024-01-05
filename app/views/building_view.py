from flask import jsonify

class BuildingView:
    @staticmethod
    def serialize_building(building):
        return {
            'id' : building.id ,
            'code' : building.code ,
            'tag' : building.tag ,
            'slug' : building.slug ,
            'name' : building.name ,
            'address' : building.address ,
            'description' : building.description ,
            'added_by': building.added_by ,
            'added_date' : building.added_date ,
            'updated_by' : building.updated_by ,
            'updated_date' : building.updated_date
        }

    @staticmethod
    def render_building(building):
        return jsonify(BuildingView.serialize_building(building))

    @staticmethod
    def render_buildings(buildings):
        result = []
        for building in buildings:
            building_dict = {
                'id' : building.id ,
                'code' : building.code ,
                'tag' : building.tag ,
                'slug' : building.slug ,
                'name' : building.name ,
                'address' : building.address ,
                'description' : building.description ,
                'added_by' : building.added_by ,
                'added_date' : building.added_date ,
                'updated_by' : building.updated_by ,
                'updated_date' : building.updated_date
            }
            result.append(building_dict)
        return jsonify( {'buildings': result} )
