import json
import os

from flask import Flask, request, render_template, redirect, url_for
from uuid import uuid4

from werkzeug.utils import secure_filename

from parsers.google import parse_html
from parsers.relaxdays import get_items

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # wir nehmen an, dass die HTML-Datei <16MB ist
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['SESSION_FOLDER'] = 'sessions'

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['SESSION_FOLDER'], exist_ok=True)


@app.route('/', methods=['GET', 'POST'])
def start():
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
                return "Dies waren nicht die richtigen Dateien."
        if len(categories) == 0:
            return "Konnte keine Kategorie in der HTML-Datei fidnen."
        f['categories'] = list(categories)
        f['uuid'] = uuid4().hex
        with open(os.path.join(app.config['SESSION_FOLDER'], f['uuid']), 'w') as fh:
            json.dump(f, fh)
        return redirect(url_for('selection', uuid=f['uuid']))


@app.route('/<uuid>', methods=['GET'])
def selection(uuid):
    with open(os.path.join(app.config['SESSION_FOLDER'], uuid), 'r') as fh:
        f = json.load(fh)
    return f  # todo: return template/overview


@app.route('/<uuid>/next', methods=['GET'])
def get_next(uuid):
    get_items('Ente')
    return "something"


if __name__ == '__main__':
    app.run()
