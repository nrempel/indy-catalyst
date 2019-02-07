import logging

from typing import Callable

from ...base_handler import BaseHandler
from ....wallet.base import BaseWallet
from ....storage.base import BaseStorage

# from ..messages.connection_invitation import ConnectionInvitation

from ..messages.connection_response import ConnectionResponse, ConnectionResponseDidDoc


class ConnectionRequestHandler(BaseHandler):
    def __init__(self, message) -> None:
        self.logger = logging.getLogger(__name__)
        self.message = message

    async def handle(self, wallet: BaseWallet, storage: BaseStorage, message_sender):
        pairwise_info = await wallet.create_pairwise(
            their_did=self.message.did, their_verkey=self.message.did_doc.key
        )

        message = ConnectionResponse(
            did=pairwise_info.my_did,
            did_doc=ConnectionResponseDidDoc(
                key=pairwise_info.my_verkey, endpoint="http://172.17.0.1:10001"
            ),
        )

        await message_sender(message, self.message.did_doc.endpoint)

        return message
