from parser.parser import Parser #Parser class
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename #to store file uploaded by a user
from database import Database #Database class to store users
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads' #to config folder to save uploaded resumes
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#home route
@app.route("/")
def landing(name=None):
    return render_template("landingPage.html", name=name);
    #return render_template("/portfolio_templates/default_template.html", name=name);

#edit resume fields route
@app.route("/fill")
def fill(name=None):
    return render_template("fillResume.html", name=name);

 #POST route for final resume fields   
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
    skills = resumeParser.skillParser()
    education = resumeParser.schoolParser()
    experience = resumeParser.experienceParser()
    data = {
        "fileName": filename,
        "email": email,
        "name": name,
        "phoneNumber": phoneNumber,
        "title": "title",
        "education": education,
        "skills": skills,
        "projects": projectP,
        "experience": experience
    }
    return render_template("fillResume.html", data=data)

#add user route
@app.route("/adduser",  methods=['POST'])
def load_user():
    data = {
        "email": request.form['email'],
        "name": request.form['name'],
        "phoneNumber": request.form['phoneNumber'],
        "title": request.form['title'],
        "education": request.form['education'],
        "skills": request.form['skills'],
        "projects": request.form['projects'],
        "experience": request.form['experience'],
        "fileName": request.form["fileName"]
    }
    id = addToDatabase(data)
    return render_template("confirmation.html", id=id)

#user portfolio
@app.route("/user/<id>")
def showUser(id):
    dataBase = Database()
    userList = dataBase.getUser(id)
    data = {
        "id": userList[0][0],
        "name": userList[0][1],
        "email": userList[0][2],
        "phoneNumber": userList[0][3],
        "title": userList[0][4],
        "education": userList[0][5],
        "projects": userList[0][6],
        "skills": userList[0][7],
        "experience": userList[0][8],
    }
    skills = userList[0][7].split(',')
    return render_template("/portfolio_templates/default_template.html", data=data, skills=skills)

#show resume
@app.route("/user/resume/<id>")
def showResume(id):
    dataBase = Database()
    userList = dataBase.getUser(id)
    return render_template("/portfolio_templates/showResume.html", fileName=userList[0][9])

#about us
@app.route("/aboutus")
def aboutUs():
    return render_template("aboutUs.html")

#add to database
def addToDatabase(data):
    dataBase = Database()
    id = dataBase.insert(data)
    return id