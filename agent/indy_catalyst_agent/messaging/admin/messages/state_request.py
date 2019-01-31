"""
Represents a state request
"""
from typing import List, Text

from marshmallow import Schema, fields, post_load

from ...agent_message import HandleableAgentMessage
from ...message_types import MessageTypes

from ..handlers.state_request_handler import StateRequestHandler


class StateRequest(HandleableAgentMessage):
    def __init__(self, content):
        self._content = content

    @property
    def handler(self):
        return StateRequestHandler(self)

    @property
    # Avoid clobbering builtin property
    def _type(self) -> str:
        return MessageTypes.ADMIN_STATE_REQUEST.value

    @property
    # Avoid clobbering builtin property
    def content(self) -> str:
        return self._content

    @classmethod
    def deserialize(cls, obj):
        return StateRequestSchema().load(obj)

    def serialize(self):
        return StateRequestSchema().dump(self)


class StateRequestSchema(Schema):
    # Avoid clobbering builtin property
    _type = fields.Str(data_key="@type", required=True)
    content = fields.Constant(None, allow_none=True)

    @post_load
    def make_model(self, data: dict) -> StateRequest:
        del data["_type"]
        return StateRequest(**data)
