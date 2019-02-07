import logging

from typing import Callable

from ....base_handler import BaseHandler
from .....wallet.base import BaseWallet
from .....storage.base import BaseStorage

from ..messages.state import State, StateContent

# from ..messages.connection_invitation import StateRequest


class StateRequestHandler(BaseHandler):
    def __init__(self, message: "StateRequest") -> None:
        self.logger = logging.getLogger(__name__)
        self.message = message

    async def handle(self, wallet: BaseWallet, storage: BaseStorage, message_sender) -> State:

        message = State(content=StateContent(initialized=False))
        return message
