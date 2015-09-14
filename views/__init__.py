#-*- encoding: utf-8 -*-

from index_view import index_blueprint
from log_view import log_blueprint
from login_view import login_blueprint
from join_view import join_blueprint


def register_views(app):
    app.register_blueprint(index_blueprint)
    app.register_blueprint(log_blueprint)
    app.register_blueprint(login_blueprint)
    app.register_blueprint(join_blueprint)
