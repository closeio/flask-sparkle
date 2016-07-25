from flask_admin.contrib.mongoengine import ModelView

from flask_sparkle.documents import *

class ApplicationAdminView(ModelView):
    list_display = ['name', 'slug', 'latest_version_string']

def register(admin):
    admin.add_view(ApplicationAdminView(Application, name='Sparkle'))
