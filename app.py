import json
import os
import sqlite3

from flask import Flask, request, render_template, redirect, url_for, g
from uuid import uuid4

from werkzeug.utils import secure_filename

from parsers.google import parse_html

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # wir nehmen an, dass die HTML-Datei <16MB ist
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['SESSION_FOLDER'] = 'sessions'

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['SESSION_FOLDER'], exist_ok=True)


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect("rd-daten/daten.db")
        db.row_factory = sqlite3.Row
    return db


# this code is a mess, and I am sorry 🙈
@app.route('/', methods=['GET'])
def start():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def uplaod():
    if request.method == 'GET':
        return render_template('upload.html')
    elif request.method == 'POST':
        f = request.form.to_dict()
        files = request.files.getlist("files[]")
        if len(files) <= 0:
            return "Keine Datei hochgeladen!"
        f['files'] = []
        categories = set()
        for html in files:
            path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(html.filename))
            f['files'].append(path)
            html.save(path)
            try:
                if len(categories) == 0:
                    categories = parse_html(path)
                else:
                    categories = categories.intersection(parse_html(path))
            except AttributeError:
                return "Dies war(en) nicht die richtige(n) Datei(en)."
        if len(categories) == 0:
            return "Konnte keine Kategorie in der HTML-Datei finden."
        f['categories'] = list(categories)
        f['uuid'] = uuid4().hex
        with open(os.path.join(app.config['SESSION_FOLDER'], f['uuid']), 'w') as fh:
            json.dump(f, fh)
        return redirect(url_for('selection', uuid=f['uuid']))

@app.route('/swipe', methods=['GET'])
def swipe():
    return render_template('swipe.html')

@app.route('/result', methods=['GET'])
def result():
    return render_template('result.html')


@app.route('/<uuid>', methods=['GET'])
def selection(uuid):
    # todo: Merkliste übermitteln
    try:
        with open(os.path.join(app.config['SESSION_FOLDER'], uuid), 'r') as fh:
            f = json.load(fh)
    except FileNotFoundError:
        return "Session existiert nicht"
    return f  # todo: return template/overview instead


# dies ist der Endpunkt, der über Javascript für neue Daten abgerufen werden muss
@app.route('/<uuid>/next', methods=['GET'])
def get_next(uuid):
    with open(os.path.join(app.config['SESSION_FOLDER'], uuid), 'r') as fh:
        f = json.load(fh)
    if 'current_category' not in f:
        f['current_category'] = 0
        f['current_product'] = 0
        f['current_turn'] = 1  # wird erhöht, wenn alle Produkte einmal durchlaufen wurden.
        f['category_rating'] = {}
        for x, cat in enumerate(f['categories']):
            f['category_rating'][x] = 0
    c = get_db().cursor()
    sql = 'SELECT * FROM "{}" WHERE id>={} AND price<={} LIMIT 1'.format(f['categories'][f['current_category']], f['current_product'], f['max_price'])  # woohooo SQL injektion!
    print(sql)
    c.execute(sql)
    rows = c.fetchall()
    if len(rows) != 1:  # überspringen, falls nichts gefunden
        f['current_product'] = 0
        f['category_rating'][f['current_category']] = -1  # ZIEL: alle Kategorie-Bewertung auf -1 kriegen
        f['current_category'] += 1
    else:
        for r in rows:
            print(dict(r))  # TODO: hier weiter machen.
    with open(os.path.join(app.config['SESSION_FOLDER'], uuid), 'w') as fh:
        json.dump(f, fh)
    return str(f)  # TODO: wenn man es ohne cast zurück gibt, schmeißt es hier einen Fehler... Just... why?


# dies ist der Endpunkt, der das Ergebnis
@app.route('/<uuid>/result/<yesno>', methods=['POST'])
def submit_result(uuid, yesno):
    return "somethingelse"




@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


if __name__ == '__main__':
    app.run()
