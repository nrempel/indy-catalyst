from .message_types import MessageTypes


from .admin.base.messages.state_request import StateRequest

from .admin.wallet_connection.messages.connect import Connect

from .admin.connections.messages.generate_invite import GenerateInvite

from .connections.messages.connection_invitation import ConnectionInvitation
from .connections.messages.connection_request import ConnectionRequest
from .connections.messages.connection_response import ConnectionResponse

from .credentials.messages.credential_offer import CredentialOffer
from .credentials.messages.credential_request import CredentialRequest
from .credentials.messages.credential import Credential

from .proofs.messages.proof_request import ProofRequest
from .proofs.messages.proof import Proof

from .routing.messages.forward import Forward


class MessageParseError(Exception):
    pass


class MessageFactory:
    """
    Message factory for deserializing message json and obtaining relevant
    message class
    """

    @classmethod
    def make_message(cls, obj):
        """
        Given a dict describing a message, this method
        returns an instance of the related message class.
        """

        if not obj.get("@type"):
            raise MessageParseError("Message does not contain '@type' parameter")

        # Admin Base Messages
        if obj["@type"] == MessageTypes.ADMIN_BASE_STATE_REQUEST.value:
            return StateRequest.deserialize(obj)

        # Admin Wallet Connection Messages
        if obj["@type"] == MessageTypes.ADMIN_WALLET_CONNECTION_CONNECT.value:
            return Connect.deserialize(obj)

        # Admin Connection Messages
        if obj["@type"] == MessageTypes.ADMIN_CONNECTION_GENERATE_INVITE.value:
            return GenerateInvite.deserialize(obj)

        # Connection Messages
        if obj["@type"] == MessageTypes.CONNECTION_INVITATION.value:
            return ConnectionInvitation.deserialize(obj)
        elif obj["@type"] == MessageTypes.CONNECTION_REQUEST.value:
            return ConnectionRequest.deserialize(obj)
        elif obj["@type"] == MessageTypes.CONNECTION_RESPONSE.value:
            return ConnectionResponse.deserialize(obj)

        # Credential Messages
        elif obj["@type"] == MessageTypes.CREDENTIAL.value:
            return Credential.deserialize(obj)
        elif obj["@type"] == MessageTypes.CREDENTIAL_OFFER.value:
            return CredentialOffer.deserialize(obj)
        elif obj["@type"] == MessageTypes.CREDENTIAL_REQUEST.value:
            return CredentialRequest.deserialize(obj)

        # Proof Messages
        elif obj["@type"] == MessageTypes.PROOF_REQUEST.value:
            return ProofRequest.deserialize(obj)
        elif obj["@type"] == MessageTypes.PROOF.value:
            return Proof.deserialize(obj)

        # Routing Messages
        elif obj["@type"] == MessageTypes.FORWARD.value:
            return Forward.deserialize(obj)

        else:
            raise MessageParseError(f"Unrecognized message type {obj['@type']}")

