#-*- encoding: utf-8 -*-

from index_view import index_blueprint

def register_views(app):
    app.register_blueprint(index_blueprint)
