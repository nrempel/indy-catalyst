import logging

from typing import Callable

from ....base_handler import BaseHandler
from .....wallet.base import BaseWallet
from .....storage.base import BaseStorage

from ...base.messages.state import State, StateContent

# from ..messages.connect import Connect


class ConnectHandler(BaseHandler):
    def __init__(self, message: "Connect") -> None:
        self.logger = logging.getLogger(__name__)
        self.message = message

    async def handle(self, wallet: BaseWallet, storage: BaseStorage) -> State:
        await wallet.open()

        initialized = wallet.opened
        pairwise = await wallet.get_pairwise_list()

        pairwise_connections = []
        for pair in pairwise:
            self.logger.info(pair)

        message = State(
            content=StateContent(
                initialized=initialized, pairwise_connections=pairwise_connections, 
            )
        )
        return message
