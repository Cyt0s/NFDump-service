from core.parsers.serializers.file_serializer import FileSerializer
from core.models.flow_object import FlowObject
import pandas
import json


class JsonSerializer(FileSerializer):
    def __init__(self):
        pass

    def serialize(self, object_to_serialize: str) -> FlowObject:
        object_dict = json.loads(object_to_serialize)
        return FlowObject(data=pandas.DataFrame.from_dict(object_dict))

    def deserialize(self, object_to_deserialize: FlowObject) -> str:
        return object_to_deserialize.data.to_json()

    def get_type(self):
        return "json"
