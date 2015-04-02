from flask_views.db.mongoengine.detail import DetailView

from flask_sparkle import sparkle
from flask_sparkle.documents import Application


class AppcastView(DetailView):
    get_fields = { 'slug': 'slug' }
    document_class = Application
    template_name = 'appcast.xml'

sparkle.add_url_rule('/<slug>/appcast.xml', view_func=AppcastView.as_view('appcast'))


try:
    from flask.ext.mongorest.views import ResourceView
    from flask_sparkle.resources import ApplicationResource
    from flask.ext.mongorest import methods
    from flask.ext.mongorest.authentication import AuthenticationBase
    from flask.ext.login import current_user


    class SparkleAuthentication(AuthenticationBase):
        def authorized(self, obj=None):
            return 'sparkle' in getattr(current_user, 'roles', [])

    class ApplicationView(ResourceView):
        resource = ApplicationResource
        methods = [methods.Create, methods.Update, methods.Fetch, methods.List]
        authentication_methods = [SparkleAuthentication]

except ImportError:
    pass
