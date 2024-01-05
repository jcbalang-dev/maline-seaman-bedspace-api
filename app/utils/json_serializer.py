import json
from decimal import Decimal
from datetime import datetime

class JSONSerializer(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        elif isinstance(obj, datetime):
            return obj.isoformat()
        elif isinstance(obj, str):
            return obj
        elif isinstance(obj, int):
            return obj
        elif isinstance(obj, float):
            return obj
        elif isinstance(obj, bool):
            return obj
        elif obj is None:
            return None
        return super(JSONSerializer, self).default(obj)
    