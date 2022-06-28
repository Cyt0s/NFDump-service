from core.normalizers.normalizer import Normalizer
from core.models.flow_object import FlowObject
from core.models.flow_scheduler import FlowScheduler


class NetflowNormalizer(Normalizer):
    def __init__(self, flow_scheduler: FlowScheduler):
        self.__flow_scheduler = flow_scheduler

    def normalize(self, parsed_object: FlowObject):
        for logic in self.__flow_scheduler.preprocess_logics:
            logic.run(parsed_object)
        for logic in self.__flow_scheduler.process_logics:
            logic.run(parsed_object)
        return parsed_object
