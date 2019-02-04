import logging

from typing import Callable

from ....base_handler import BaseHandler
from .....wallet.base import BaseWallet

from ....connections.messages.connection_invitation_indy_agent import (
    ConnectionInvitation
)

from ..messages.invite_generated import InviteGenerated


# from ..messages.generate_invite import GenerateInvite


class GenerateInviteHandler(BaseHandler):
    def __init__(self, message: "GenerateInvite") -> None:
        self.logger = logging.getLogger(__name__)
        self.message = message

    async def handle(self, wallet: BaseWallet) -> ConnectionInvitation:
        await wallet.open()

        # initialized = wallet.opened
        # pairwise = await wallet.get_pairwise_list()

        # TODO: make this cli param or something
        public_url = "http://172.17.0.1:10000"

        invite = ConnectionInvitation(endpoint=public_url, label="label")

        invite_encoded = invite.base64_encode()
        invite_url = f"{public_url}?c_i={invite_encoded}"

        invite_generated = InviteGenerated(invite_url)

        return invite_generated
        # pairwise_GenerateInviteions = []
        # for pair in pairwise:
        #     self.logger.info(pair)

        # message = State(
        #     content=StateContent(
        #         initialized=initialized, pairwise_GenerateInviteions=pairwise_GenerateInviteions,
        #     )
        # )
        # return message
