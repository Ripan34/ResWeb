import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def landing(name=None):
    return render_template("landingPage.html", name=name);

@app.route("/fill")
def fill(name=None):
    return render_template("fillResume.html", name=name);

@app.route("/resume", methods=['POST'])
def upload_res():
    data = request.files['doc_file']
    filename = secure_filename(data.filename)
    data.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return render_template("fillResume.html", fileName=filename);