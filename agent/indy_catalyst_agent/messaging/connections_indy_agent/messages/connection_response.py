"""
Represents a connection response message.
"""

from marshmallow import Schema, fields, post_load

from ...agent_message import AgentMessage
from ...message_types import MessageTypes
from ...validators import must_not_be_none

from ..handlers.connection_response_handler import ConnectionResponseHandler


# TODO: move to models?
class ConnectionResponseDidDoc(AgentMessage):
    def __init__(self, key: str, endpoint: str):
        self.key = key
        self.endpoint = endpoint

    @classmethod
    def deserialize(cls, obj):
        return ConnectionResponseDidDocSchema().load(obj)

    def serialize(self):
        return ConnectionResponseDidDocSchema().dump(self)


class ConnectionResponseDidDocSchema(Schema):
    # Avoid clobbering builtin property
    key = fields.Str(required=True)
    endpoint = fields.Str(required=True)

    @post_load
    def make_model(self, data: dict) -> ConnectionResponseDidDoc:
        return ConnectionResponseDidDoc(**data)


class ConnectionResponse(AgentMessage):
    def __init__(self, did: str, did_doc: ConnectionResponseDidDoc):
        self.handler = ConnectionResponseHandler(self)
        self.did = did
        self.did_doc = did_doc

    @property
    # Avoid clobbering builtin property
    def _type(self):
        return MessageTypes.CONNECTION_RESPONSE.value

    @classmethod
    def deserialize(cls, obj):
        return ConnectionResponseSchema().load(obj)

    def serialize(self):
        return ConnectionResponseSchema().dump(self)


class ConnectionResponseSchema(Schema):
    # Avoid clobbering builtin property
    _type = fields.Str(data_key="@type", required=True)
    did = fields.Str(data_key="DID", required=True)
    did_doc = fields.Nested(
        ConnectionResponseDidDocSchema,
        data_key="DIDDoc",
        validate=must_not_be_none,
        required=True,
    )

    @post_load
    def make_model(self, data: dict) -> ConnectionResponse:
        print(data)
        del data["_type"]
        return ConnectionResponse(**data)
