# -*- encoding: utf-8 -*- #


from flask import Blueprint, request, render_template, redirect, url_for, session, g
import os
import sys

setting_video_blueprint = Blueprint('setting_video', __name__)

@setting_video_blueprint.route('/setting_video', methods=['GET','POST'])
def log():
    if request.method == 'POST':
        e1 = os.system('sudo pkill -9 uv4l')
        e2 = os.system('uv4l --driver raspicam --auto-video_nr --width '
                + request.form['width'] + ' --height '
                + request.form['height'] + ' --encoding mjpeg')
    else:
        e1 = os.system('sudo pkill -9 uv4l')
        e2 = os.system('uv4l --driver raspicam --auto-video_nr --width '
                +request.args.get('width')
                + ' --height '+ request.args.get('height')
                + ' --encoding mjpeg')

    if e1 and e2 is not 0:
        return "false", 404
    else:
        return "ok", 200
