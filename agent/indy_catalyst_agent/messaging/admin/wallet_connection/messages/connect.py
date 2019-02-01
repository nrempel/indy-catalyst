"""
Represents a Connect request
"""
from typing import Dict, List, Text

from marshmallow import Schema, fields, post_load

from ....agent_message import AgentMessage
from ....message_types import MessageTypes
from ....validators import must_not_be_none

from ..handlers.connect_handler import ConnectHandler


class Connect(AgentMessage):
    def __init__(self, name: Text, passphrase: Text):
        self.name = name
        self.passphrase = passphrase

    @property
    # Avoid clobbering builtin property
    def _type(self) -> str:
        return MessageTypes.ADMIN_WALLET_CONNECTION_CONNECT.value

    @property
    def handler(self) -> ConnectHandler:
        return ConnectHandler(self)

    @classmethod
    def deserialize(cls, obj):
        return ConnectSchema().load(obj)

    def serialize(self):
        return ConnectSchema().dump(self)


class ConnectSchema(Schema):
    # Avoid clobbering builtin property
    _type = fields.Str(data_key="@type", required=True)
    name = fields.Str(required=True)
    passphrase = fields.Str(required=True)

    @post_load
    def make_model(self, data: dict) -> Connect:
        del data["_type"]
        return Connect(**data)
