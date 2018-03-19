from cleancat import URL, Bool, DateTime, List, Schema, String
from cleancat.mongo import MongoEmbedded

from flask_sparkle import documents


class Version(Schema):
    date_published = DateTime(required=False)
    title = String(required=False)
    description = String(required=False)
    update_url = URL(required=False)
    version = String(required=False)
    short_version = String(required=False)
    length = String(required=False)
    dsa_signature = String(required=False)
    is_published = Bool(required=False)


class Application(Schema):
    name = String()
    slug = String()
    versions = List(MongoEmbedded(documents.Version, Version), required=False)
