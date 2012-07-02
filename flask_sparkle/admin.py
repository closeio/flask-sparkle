from flask.ext.admin.contrib.mongoengine.view import ModelView

from flask_sparkle.documents import *

class ApplicationView(ModelView):
    list_columns = ['name', 'slug', 'latest_version']

def register(admin):
    admin.add_view(ApplicationView(Application, name='Application', endpoint='sparkle/application', category='Sparkle'))
