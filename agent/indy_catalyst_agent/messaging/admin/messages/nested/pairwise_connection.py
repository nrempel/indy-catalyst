from typing import Text

from marshmallow import Schema, fields

from ....validators import must_not_be_none


class Metadata:
    def __init__(self, label: Text, their_endpoint: Text, their_vk: Text, my_vk: Text):
        self.label = label
        self.their_endpoint = their_endpoint
        self.their_vk = their_vk
        self.my_vk = my_vk


class MetadataSchema(Schema):
    label = fields.Str(required=True)
    their_endpoint = fields.Str(required=True)
    their_vk = fields.Str(required=True)
    my_vk = fields.Str(required=True)


class PairwiseConnection:
    def __init__(self, my_did: Text, their_did: Text, metadata: Metadata):
        self.my_did = my_did
        self.their_did = their_did
        self.metadata = metadata


class PairwiseConnectionSchema(Schema):
    my_did = fields.Str(required=True)
    their_did = fields.Str(required=True)
    endpoint = fields.Nested(MetadataSchema, validate=must_not_be_none, required=True)
