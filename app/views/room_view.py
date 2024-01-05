from flask import jsonify
from app.models.building_model import BuildingModel
from app.models.user_model import UserModel

building_model = BuildingModel()
user_model = UserModel()

class RoomView:
    @staticmethod
    def serialize_room(room):
        
        building = building_model.get(room.building_id)
        building_dict = {
            'building_id' : building.id ,
            'building_code' : building.code ,
            'building_tag' : building.tag ,
            'building_slug' : building.slug ,
            'building_name' : building.name ,
            'building_address' : building.address ,
            'building_description' : building.description
        }

        added_by = user_model.get(room.added_by)
        added_by_dict = {
            'id' : added_by.id,
            'last_name' : added_by.last_name,
            'first_name' : added_by.first_name,
            'middle_name' : added_by.middle_name,
            'user_id' : added_by.user_id,
            'email' : added_by.email,
            'status' : added_by.status,
        }

        updated_by = user_model.get(room.updated_by)
        updated_by_dict = {
            'id' : updated_by.id,
            'last_name' : updated_by.last_name,
            'first_name' : updated_by.first_name,
            'middle_name' : updated_by.middle_name,
            'user_id' : updated_by.user_id,
            'email' : updated_by.email,
            'status' : updated_by.status,
        }

        return {
            "id" : room.id ,
            "building" : building_dict ,
            "number" : room.number ,
            "code" : room.code ,
            "tag" : room.tag ,
            "slug" : room.slug ,
            "rate" : room.rate ,
            "bed_capacity" : room.bed_capacity ,
            "availability" : room.availability ,
            "description" : room.description ,
            "added_by" : added_by_dict ,
            "added_date" : room.added_date ,
            "updated_by" : updated_by_dict ,
            "updated_date" : room.updated_date
        }

    @staticmethod
    def render_room(room):
        return jsonify(RoomView.serialize_room(room))

    @staticmethod
    def render_rooms(rooms):
        result = []
        for room in rooms:
            building = building_model.get(room.building_id)
            building_dict = {
                'building_id' : building.id ,
                'building_code' : building.code ,
                'building_tag' : building.tag ,
                'building_slug' : building.slug ,
                'building_name' : building.name ,
                'building_address' : building.address ,
                'building_description' : building.description
            }

            added_by = user_model.get(room.added_by)
            added_by_dict = {
                'id' : added_by.id,
                'last_name' : added_by.last_name,
                'first_name' : added_by.first_name,
                'middle_name' : added_by.middle_name,
                'user_id' : added_by.user_id,
                'email' : added_by.email,
                'status' : added_by.status,
            }

            updated_by = user_model.get(room.updated_by)
            updated_by_dict = {
                'id' : updated_by.id,
                'last_name' : updated_by.last_name,
                'first_name' : updated_by.first_name,
                'middle_name' : updated_by.middle_name,
                'user_id' : updated_by.user_id,
                'email' : updated_by.email,
                'status' : updated_by.status,
            }

            dict = {
                "id" : room.id ,
                "building" : building_dict ,
                "number" : room.number ,
                "code" : room.code ,
                "tag" : room.tag ,
                "slug" : room.slug ,
                "rate" : room.rate ,
                "bed_capacity" : room.bed_capacity ,
                "availability" : room.availability ,
                "description" : room.description ,
                "added_by" : added_by_dict ,
                "added_date" : room.added_date ,
                "updated_by" : updated_by_dict ,
                "updated_date" : room.updated_date
            }
            result.append(dict)
        return jsonify( { 'rooms' : result } )
