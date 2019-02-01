"""
Represents a state request
"""
from typing import Dict, List, Text

from marshmallow import Schema, fields, post_load

from ....agent_message import AgentMessage
from ....message_types import MessageTypes
from ....validators import must_not_be_none

from .nested.pairwise_connection import PairwiseConnection, PairwiseConnectionSchema


class StateContent:
    def __init__(
        self,
        initialized: bool,
        agent_name: Text = None,
        pairwise_connections: List[PairwiseConnection] = None,
    ):

        self.initialized = initialized
        self.agent_name = agent_name
        self.pairwise_connections = pairwise_connections


class StateContentSchema(Schema):
    initialized = fields.Bool(required=True)
    agent_name = fields.Str(required=True)
    pairwise_connections = fields.Nested(
        PairwiseConnectionSchema, many=True, validate=must_not_be_none, required=True
    )


class State(AgentMessage):
    def __init__(self, content: StateContent = None):
        self._content = content

    @property
    # Avoid clobbering builtin property
    def _type(self) -> str:
        return MessageTypes.ADMIN_BASE_STATE.value

    @property
    def content(self) -> Dict:
        return self._content

    @classmethod
    def deserialize(cls, obj):
        return StateSchema().load(obj)

    def serialize(self):
        return StateSchema().dump(self)


class StateSchema(Schema):
    # Avoid clobbering builtin property
    _type = fields.Str(data_key="@type", required=True)
    content = fields.Nested(StateContentSchema)

    @post_load
    def make_model(self, data: dict) -> State:
        del data["_type"]
        return State(**data)
