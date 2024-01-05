from flask import jsonify

class RoomBedSpaceView:
    @staticmethod
    def serialize_room_bedspace(room_bedspace):
        return {
            'id': room_bedspace.id,
            'room_id': room_bedspace.room_id,
            'number': room_bedspace.number,
            'code': room_bedspace.code,
            'tag': room_bedspace.tag,
            'slug': room_bedspace.slug,
            'availability': room_bedspace.availability,
            'description': room_bedspace.description,
            'added_by': room_bedspace.added_by,
            'added_date': room_bedspace.added_date.strftime("%Y-%m-%d %H:%M:%S"),
            'updated_by': room_bedspace.updated_by,
            'updated_date': room_bedspace.updated_date.strftime("%Y-%m-%d %H:%M:%S"),
        }

    @staticmethod
    def render_room_bedspace(room_bedspace):
        return jsonify(RoomBedSpaceView.serialize_room_bedspace(room_bedspace))

    @staticmethod
    def render_room_bedspaces(room_bedspaces):
        result = []
        for room_bedspace in room_bedspaces:
            room_bedspace_dict = {
                'id': room_bedspace[0],
                'room_id': room_bedspace[1],
                'number': room_bedspace[2],
                'code': room_bedspace[3],
                'tag': room_bedspace[4],
                'slug': room_bedspace[5],
                'availability': room_bedspace[6],
                'description': room_bedspace[7],
                'added_by': room_bedspace[8],
                'added_date': room_bedspace[9].strftime("%Y-%m-%d %H:%M:%S"),
                'updated_by': room_bedspace[10],
                'updated_date': room_bedspace[11].strftime("%Y-%m-%d %H:%M:%S"),
            }
            result.append(room_bedspace_dict)

        return {'room_bedspaces': result}
