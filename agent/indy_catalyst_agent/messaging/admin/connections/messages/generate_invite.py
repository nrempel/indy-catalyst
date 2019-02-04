"""
Represents a generate_invite request
"""
from typing import Dict, List, Text

from marshmallow import Schema, fields, post_load

from ....agent_message import AgentMessage
from ....message_types import MessageTypes
from ....validators import must_not_be_none

from ..handlers.generate_invite_handler import GenerateInviteHandler


class GenerateInvite(AgentMessage):
    def __init__(self):
        pass

    @property
    # Avoid clobbering builtin property
    def _type(self) -> str:
        return MessageTypes.ADMIN_CONNECTION_GENERATE_INVITE.value

    @property
    def handler(self) -> GenerateInviteHandler:
        return GenerateInviteHandler(self)

    @classmethod
    def deserialize(cls, obj):
        return GenerateInviteSchema().load(obj)

    def serialize(self):
        return GenerateInviteSchema().dump(self)


class GenerateInviteSchema(Schema):
    # Avoid clobbering builtin property
    _type = fields.Str(data_key="@type", required=True)

    @post_load
    def make_model(self, data: dict) -> GenerateInvite:
        del data["_type"]
        return GenerateInvite(**data)
