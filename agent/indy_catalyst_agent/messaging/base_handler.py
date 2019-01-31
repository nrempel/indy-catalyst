from abc import ABC, abstractmethod

from .agent_message import AgentMessage


class BaseHandler(ABC):
    @abstractmethod
    def __init__(self, message: AgentMessage) -> None:
        pass

    @abstractmethod
    async def handle(self) -> AgentMessage:
        pass
