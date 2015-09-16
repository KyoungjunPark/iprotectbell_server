#-*- encoding: utf-8 -*-

from log_view import log_blueprint
from login_view import login_blueprint
from join_view import join_blueprint
from send_log_view import send_log_blueprint
from setting_video_view import setting_video_blueprint
from door_view import door_blueprint

def register_views(app):
    app.register_blueprint(log_blueprint)
    app.register_blueprint(login_blueprint)
    app.register_blueprint(join_blueprint)
    app.register_blueprint(send_log_blueprint)
    app.register_blueprint(setting_video_blueprint)
    app.register_blueprint(door_blueprint)
