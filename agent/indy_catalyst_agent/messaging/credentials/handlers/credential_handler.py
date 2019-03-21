"""Basic message handler."""

from ...base_handler import BaseHandler, BaseResponder, RequestContext

from ..manager import CredentialManager
from ..messages.credential import Credential


class CredentialHandler(BaseHandler):
    """Message handler class for credential offers."""

    async def handle(self, context: RequestContext, responder: BaseResponder):
        """
        Message handler logic for credential offers.

        Args:
            context: request context
            responder: responder callback
        """
        self._logger.debug(f"CredentialHandler called with context {context}")
        assert isinstance(context.message, Credential)
        self._logger.info(f"Received credential: {context.message.credential_json}")

        credential = context.message.credential_json
        credential_manager = CredentialManager(context)

        await credential_manager.store_credential(credential)
