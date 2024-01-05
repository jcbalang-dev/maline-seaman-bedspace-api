from flask import jsonify

class RoomRateView:
    @staticmethod
    def serialize_room_rate(room_rate):
        return {
            'id': room_rate.id,
            'building_id': room_rate.building_id,
            'number': room_rate.number,
            'code': room_rate.code,
            'tag': room_rate.tag,
            'slug': room_rate.slug,
            'description': room_rate.description,
            'price': float(room_rate.price),
            'status': room_rate.status,
            'added_by': room_rate.added_by,
            'added_date': room_rate.added_date.strftime("%Y-%m-%d %H:%M:%S"),
            'updated_by': room_rate.updated_by,
            'updated_date': room_rate.updated_date.strftime("%Y-%m-%d %H:%M:%S"),
        }

    @staticmethod
    def render_room_rate(room_rate):
        return jsonify(RoomRateView.serialize_room_rate(room_rate))

    @staticmethod
    def render_room_rates(room_rates):
        result = []
        for room_rate in room_rates:
            room_rate_dict = {
                'id': room_rate[0],
                'building_id': room_rate[1],
                'number': room_rate[2],
                'code': room_rate[3],
                'tag': room_rate[4],
                'slug': room_rate[5],
                'description': room_rate[6],
                'price': float(room_rate[7]),
                'status': room_rate[8],
                'added_by': room_rate[9],
                'added_date': room_rate[10].strftime("%Y-%m-%d %H:%M:%S"),
                'updated_by': room_rate[11],
                'updated_date': room_rate[12].strftime("%Y-%m-%d %H:%M:%S"),
            }
            result.append(room_rate_dict)

        return {'room_rates': result}
