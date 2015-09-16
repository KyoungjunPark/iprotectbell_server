# -*- encoding: utf-8 -*-

from flask import Blueprint, request, render_template, redirect, url_for, session, g
from ..auth.commons import login_required

door_blueprint = Blueprint('door', __name__)

@door_blueprint.route('/door', methods=['POST'])
@login_required
def door():
    cur = g.db.execute('select user_id from token where user_token = ?', [request.headers.get('token')])
    g.db.commit()
    rv = cur.fetchall()
    cur.close()

    result = rv[0] if rv else None

    if result is None:
        return "incorrect token", 404

    cur = g.db.execute('update bell set open_status = ? where id = ?'
    ,[request.form['status'], result['user_id']])
    g.db.commit()
    rv = cur.fetchall()
    cur.close()

    return "ok", 200
