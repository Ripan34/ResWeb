import os
from parser.parser import Parser
from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def landing(name=None):
    #return render_template("landingPage.html", name=name);
    return render_template("/portfolio_templates/default_template.html", name=name);

@app.route("/fill")
def fill(name=None):
    return render_template("fillResume.html", name=name);
    
@app.route("/resume", methods=['POST'])
def upload_res():
    email = request.form['email']
    name = request.form['name']
    myFile = request.files['pdf_file']
    filename = secure_filename(myFile.filename)
    myFile.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    resumeParser = Parser(filename)
    phoneNumber = resumeParser.phoneNumberParser()
    projectP = resumeParser.projectsParser()
    print(projectP)
    education = resumeParser.schoolParser()
    data = {
        "fileName": filename,
        "email": email,
        "name": name,
        "phone": phoneNumber,
        "education": education
    }
    return render_template("fillResume.html", data=data)