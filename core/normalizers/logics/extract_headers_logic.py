from core.normalizers.logics.logic import Logic
from core.models.flow_object import FlowObject


class ExtractHeadersLogic(Logic):
    def __init__(self, relevant_headers: list):
        self.__relevant_headers = relevant_headers

    def run(self, flow_object: FlowObject):
        flow_object_data_copy = flow_object.data.copy()
        flow_object_data_copy = flow_object_data_copy[self.__relevant_headers]
        flow_object.data = flow_object_data_copy
