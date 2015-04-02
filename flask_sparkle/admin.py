from flask.ext.superadmin import model

from flask_sparkle.documents import *

class ApplicationAdmin(model.ModelAdmin):
    list_display = ['name', 'slug', 'latest_version_string']

def register(admin):
    admin.register(Application, ApplicationAdmin, name='Sparkle')
