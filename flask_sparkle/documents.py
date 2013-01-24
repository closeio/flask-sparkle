from mongoengine import *
from flask_common.documents import DocumentBase


class Version(EmbeddedDocument):
    date_published = DateTimeField()
    title = StringField()
    description = StringField()
    update_url = URLField()
    version = StringField()
    short_version = StringField()
    length = StringField()
    dsa_signature = StringField()
    is_published = BooleanField()


class Application(DocumentBase):
    name = StringField()
    slug = StringField(unique=True)

    versions = ListField(EmbeddedDocumentField(Version))

    def latest_version(self):
        versions = self.versions
        for version in versions:
            if version.is_published:
                return version

    def latest_version_string(self):
        latest_version = self.latest_version()
        return latest_version and latest_version.version
