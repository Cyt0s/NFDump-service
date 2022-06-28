from core.normalizers.logics.logic import Logic
from core.models.flow_object import FlowObject


class ChangeHeadersLogic(Logic):
    def __init__(self, names: dict):
        self.__names = names

    def run(self, flow_object: FlowObject):
        flow_object_data_copy = flow_object.data.copy()
        flow_object_data_copy.rename(columns=self.__names, inplace=True)
        flow_object.data = flow_object_data_copy
