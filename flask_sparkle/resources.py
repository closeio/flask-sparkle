from flask.ext.mongorest.resources import Resource
from flask_sparkle import documents, schemas


class VersionResource(Resource):
    document = documents.Version

class ApplicationResource(Resource):
    document = documents.Application
    schema = schemas.Application
    fields = ['name', 'slug', 'versions', 'date_updated', 'date_created']
    related_resources = {
        'versions': VersionResource
    }

    def get_object(self, pk, **kwargs):
        return self.get_queryset().get(slug=pk)
