from abc import ABC, abstractproperty, abstractclassmethod, abstractmethod

# from .base_handler import BaseHandler


class AgentMessage(ABC):
    @abstractproperty
    def _type(self) -> str:
        pass

    # @abstractproperty
    # def content(self) -> str:
    #     pass

    @abstractmethod
    def serialize(self) -> dict:
        pass

    @abstractclassmethod
    def deserialize(cls):
        pass


class HandleableAgentMessage(AgentMessage, ABC):
    @abstractproperty
    def handler(self) -> "BaseHandler":
        pass
