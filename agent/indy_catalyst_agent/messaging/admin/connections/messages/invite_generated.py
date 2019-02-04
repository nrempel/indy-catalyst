"""
Represents a invite_generated request
"""
from typing import Dict, List, Text

from marshmallow import Schema, fields, post_load

from ....agent_message import AgentMessage
from ....message_types import MessageTypes
from ....validators import must_not_be_none


class InviteGenerated(AgentMessage):
    def __init__(self, invite: Text):
        self.invite = invite

    @property
    # Avoid clobbering builtin property
    def _type(self) -> str:
        return MessageTypes.ADMIN_CONNECTION_INVITE_GENERATED.value

    @classmethod
    def deserialize(cls, obj):
        return InviteGeneratedSchema().load(obj)

    def serialize(self):
        return InviteGeneratedSchema().dump(self)


class InviteGeneratedSchema(Schema):
    # Avoid clobbering builtin property
    _type = fields.Str(data_key="@type", required=True)
    invite = fields.Str(required=True)

    @post_load
    def make_model(self, data: dict) -> InviteGenerated:
        del data["_type"]
        return InviteGenerated(**data)
