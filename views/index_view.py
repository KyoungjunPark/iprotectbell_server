# -*- encoding: utf-8 -*-
import json

from flask import Blueprint, request, render_template, redirect, url_for, session, g

index_blueprint = Blueprint('index', __name__)

@index_blueprint.route('/', methods=['GET'])
def home():
    cur = g.db.execute('select * from user')
    results = []
    #return render_template('home.html', entries = entries)
    return json.dumps([dict(ix) for ix in cur.fetchall()])
