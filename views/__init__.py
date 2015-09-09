#-*- encoding: utf-8 -*-

from index_view import index_blueprint
from log_view import log_blueprint

def register_views(app):
    app.register_blueprint(index_blueprint)
    app.register_blueprint(log_blueprint)
