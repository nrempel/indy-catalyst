"""
Represents a state request
"""
from typing import List, Text

from marshmallow import Schema, fields, post_load

from ...agent_message import AgentMessage
from ...message_types import MessageTypes
from ...validators import must_not_be_none

from .nested.pairwise_connection import PairwiseConnection, PairwiseConnectionSchema


class State(AgentMessage):
    def __init__(
        self,
        initialized: bool,
        agent_name: Text,
        pairwise_connections: List[PairwiseConnection],
    ):
        self.initialized = initialized
        self.agent_name = (agent_name,)
        self.pairwise_connections = pairwise_connections

    @property
    # Avoid clobbering builtin property
    def _type(self) -> str:
        return MessageTypes.ADMIN_STATE.value

    @classmethod
    def deserialize(cls, obj):
        return StateSchema().load(obj)

    def serialize(self):
        return StateSchema().dump(self)


class StateSchema(Schema):
    # Avoid clobbering builtin property
    _type = fields.Str(data_key="@type", required=True)

    initialized = fields.Bool(required=True)
    agent_name = fields.Str(required=True)
    pairwise_connections = fields.Nested(
        PairwiseConnectionSchema, many=True, validate=must_not_be_none, required=True
    )

    @post_load
    def make_model(self, data: dict) -> State:
        del data["_type"]
        return State(**data)
