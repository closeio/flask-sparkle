from flask import render_template
from flask_views.db.mongoengine.detail import DetailView

from flask_sparkle import sparkle
from flask_sparkle.documents import Application


class AppcastView(DetailView):
    get_fields = { 'slug': 'slug' }
    document_class = Application
    template_name = 'appcast.xml'

sparkle.add_url_rule('/<slug>/appcast.xml', view_func=AppcastView.as_view('appcast'))
