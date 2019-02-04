"""
Represents an invitation message for establishing connection.
"""

from base64 import b64encode
from uuid import uuid4

from marshmallow import Schema, fields, post_load

from ...agent_message import AgentMessage
from ...message_types import MessageTypes
from ...validators import must_not_be_none

from ..handlers.connection_invitation_handler import ConnectionInvitationHandler

from .nested.agent_endpoint import AgentEndpoint, AgentEndpointSchema


class ConnectionInvitation(AgentMessage):
    def __init__(self, endpoint: str, label: str, key: str = None):
        self.handler = ConnectionInvitationHandler(self)
        self.endpoint = endpoint
        self.label = label
        if not key:
            self.key = uuid4()
        else:
            self.key = key

    @property
    # Avoid clobbering builtin property
    def _type(self) -> str:
        return MessageTypes.CONNECTION_INVITE.value

    @classmethod
    def deserialize(cls, obj):
        return ConnectionInvitationSchema().load(obj)

    def serialize(self):
        return ConnectionInvitationSchema().dump(self)

    def base64_encode(self):
        return b64encode(
            bytes(ConnectionInvitationSchema().dumps(self), "utf8")
        ).decode("utf8")


class ConnectionInvitationSchema(Schema):
    # Avoid clobbering builtin property
    _type = fields.Str(data_key="@type", required=True)
    endpoint = fields.Str(required=True)
    label = fields.Str(required=True)
    key = fields.UUID(required=True)

    @post_load
    def make_model(self, data: dict) -> ConnectionInvitation:
        del data["_type"]
        return ConnectionInvitation(**data)
