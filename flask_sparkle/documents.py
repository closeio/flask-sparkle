from mongoengine import *
from common.documents import DocumentBase


class Version(EmbeddedDocument):
    date_published = DateTimeField()
    title = StringField()
    description = StringField()
    update_url = URLField()
    version = StringField()
    short_version = StringField()
    length = StringField()
    dsa_signature = StringField()


class Application(DocumentBase):
    name = StringField()
    slug = StringField()

    versions = ListField(EmbeddedDocumentField(Version))

    def latest_version(self):
        versions = self.versions
        if versions:
            return versions[-1].version
