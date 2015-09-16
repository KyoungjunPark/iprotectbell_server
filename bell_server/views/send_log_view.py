# -*- encoding: utf-8 -*-

from flask import Blueprint, request, render_template, redirect, url_for, session, g
from ..auth.commons import login_required

send_log_blueprint = Blueprint('send_log', __name__)

@send_log_blueprint.route('/send_log', methods=['POST'])
@login_required
def send_log():
    #also header id add...
    if request.method == 'POST':
        cur = g.db.execute('select user_id from token where user_token = ?'
                ,[request.headers.get('token')])
        print(request.headers.get('token'))

        g.db.commit()
        rv = cur.fetchall()
        cur.close()

        result = rv[0] if rv else None

        if result is None:
            print("incorrect token")
            return "incorrect token", 404

        cur = g.db.execute('insert into log values(?,?,?,?,?)'
                , [result['user_id'], request.form['date'], request.form['type']
                    , request.form['information'],request.form['importance']])
        g.db.commit()

    return "ok",200
