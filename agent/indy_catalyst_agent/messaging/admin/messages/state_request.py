"""
Represents a state request
"""
from typing import List, Text

from marshmallow import Schema, fields, post_load

from ...agent_message import AgentMessage
from ...message_types import MessageTypes

from ..handlers.state_request_handler import StateRequestHandler


class StateRequest(AgentMessage):
    def __init__(self, content):
        self.handler = StateRequestHandler(self)
        self._content = content

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
    content = fields.Dict(data_key="content", allow_none=True)

    @post_load
    def make_model(self, data: dict) -> StateRequest:
        del data["_type"]
        return StateRequest(**data)
