import logging

from typing import Callable

from ...base_handler import BaseHandler
from ....wallet.base import BaseWallet
from ....storage.base import BaseStorage

# from ..messages.connection_invitation import ConnectionInvitation


class ConnectionResponseHandler(BaseHandler):
    def __init__(self, message) -> None:
        self.logger = logging.getLogger(__name__)
        self.message = message

    async def handle(self, wallet: BaseWallet, storage: BaseStorage, message_sender):
        self.logger.info("hereasdasdasd")
        pass
