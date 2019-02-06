"""
Represents a connection request message.
"""

from marshmallow import Schema, fields, post_load

from ...agent_message import AgentMessage
from ...message_types import MessageTypes
from ...validators import must_not_be_none

from ..handlers.connection_request_handler import ConnectionRequestHandler


# TODO: move to models?
class ConnectionRequestDidDoc(AgentMessage):
    def __init__(self, key: str, endpoint: str):
        self.key = key
        self.endpoint = endpoint

    @classmethod
    def deserialize(cls, obj):
        return ConnectionRequestDidDocSchema().load(obj)

    def serialize(self):
        return ConnectionRequestDidDocSchema().dump(self)


class ConnectionRequestDidDocSchema(Schema):
    # Avoid clobbering builtin property
    key = fields.Str(required=True)
    endpoint = fields.Str(required=True)

    @post_load
    def make_model(self, data: dict) -> ConnectionRequestDidDoc:
        return ConnectionRequestDidDoc(**data)


class ConnectionRequest(AgentMessage):
    def __init__(self, label: str, did: str, did_doc: ConnectionRequestDidDoc):
        self.handler = ConnectionRequestHandler(self)
        self.label = label
        self.did = did
        self.did_doc = did_doc

    @property
    # Avoid clobbering builtin property
    def _type(self):
        return MessageTypes.CONNECTION_REQUEST.value

    @classmethod
    def deserialize(cls, obj):
        return ConnectionRequestSchema().load(obj)

    def serialize(self):
        return ConnectionRequestSchema().dump(self)


class ConnectionRequestSchema(Schema):
    # Avoid clobbering builtin property
    _type = fields.Str(data_key="@type", required=True)
    label = fields.Str(required=True)
    did = fields.Str(data_key="DID", required=True)
    did_doc = fields.Nested(
        ConnectionRequestDidDocSchema,
        data_key="DIDDoc",
        validate=must_not_be_none,
        required=True,
    )

    @post_load
    def make_model(self, data: dict) -> ConnectionRequest:
        print(data)
        del data["_type"]
        return ConnectionRequest(**data)
