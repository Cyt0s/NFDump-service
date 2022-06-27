from core.parsers.serializers.file_serializer import FileSerializer
import json


class JsonSerializer(FileSerializer):
    def __init__(self):
        pass

    def serialize(self, object_to_serialize: str) -> dict:
        serialized_object = json.loads(object_to_serialize)
        return serialized_object

    def deserialize(self, object_to_deserialize: dict) -> str:
        return json.dumps(object_to_deserialize)

    def get_type(self):
        return "json"
