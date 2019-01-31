"""
Represents a state request
"""
from typing import Text

from marshmallow import Schema, fields, post_load

from ...agent_message import AgentMessage
from ...message_types import MessageTypes
from ...validators import must_not_be_none

from ..handlers.state_request_handler import StateRequestHandler

from ....models.agent_endpoint import AgentEndpoint, AgentEndpointSchema


class StateRequest(AgentMessage):
    def __init__(self, initialized: bool, agent_name: Text):
        self.handler = StateRequestHandler(self)

        self.initialized = initialized
        self.agent_name = agent_name

    @property
    # Avoid clobbering builtin property
    def _type(self) -> str:
        return MessageTypes.ADMIN_STATE_REQUEST.value

    @classmethod
    def deserialize(cls, obj):
        return StateRequestSchema().load(obj)

    def serialize(self):
        return StateRequestSchema().dump(self)


class StateRequestSchema(Schema):
    # Avoid clobbering builtin property
    _type = fields.Str(data_key="@type", required=True)

    initialized = fields.Bool(required=True)
    agent_name = fields.Str(required=True)
    
    @post_load
    def make_model(self, data: dict) -> StateRequest:
        del data["_type"]
        return StateRequest(**data)
