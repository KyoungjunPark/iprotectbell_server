# -*- encoding: utf-8 -*-
import json

from flask import Blueprint, request, render_template, redirect, url_for, session, g

log_blueprint = Blueprint('log', __name__)

@log_blueprint.route('/log', methods=['GET'])
def log():
    cur = g.db.execute('select * from log')
    return json.dumps([dict(ix) for ix in cur.fetchall()])
