from flask.ext.mongorest.resources import Resource
from flask_sparkle.documents import Application, Version
from mongoengine.queryset import Q


class VersionResource(Resource):
    document = Version

class ApplicationResource(Resource):
    document = Application
    fields = ['name', 'slug', 'versions', 'date_updated', 'date_created']
    related_resources = {
        'versions': VersionResource
    }

    def get_object(self, pk):
        return self.get_queryset().get(slug=pk)