from abc import ABC, abstractmethod


class FileSerializer(ABC):
    @abstractmethod
    def serialize(self, object_to_serialize):
        pass

    @abstractmethod
    def deserialize(self, object_to_deserialize):
        pass

    @abstractmethod
    def get_type(self):
        pass
