# -*- encoding: utf-8 -*-
import json

from flask import Blueprint, request, render_template, redirect, url_for, session, g
from ..auth.commons import login_required

log_blueprint = Blueprint('log', __name__)

@log_blueprint.route('/log', methods=['GET'])
@login_required
def log():
    cur = g.db.execute('select user_id from token where user_token = ?'
            ,[request.headers.get('token')])
    g.db.commit()
    rv = cur.fetchall()
    cur.close()

    result = rv[0] if rv else None

    if result is None:
        return "incorrect token", 404

    cur = g.db.execute('select date, type, information, importance from log where user_id = ?'
            ,[result['user_id']])
    g.db.commit()

    return json.dumps([dict(ix) for ix in cur.fetchall()])
