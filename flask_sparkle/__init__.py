from flask import Blueprint

sparkle = Blueprint('sparkle', __name__, template_folder='templates')

import flask_sparkle.views
