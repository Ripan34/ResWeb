import sys
from database import Database
#sys.path.append("/parser")
# from parser.parser import Parser
# filename = "RipandeepSinghCurrent_Resume.pdf"
# resumeParser = Parser(filename)
# phoneNumber = resumeParser.phoneNumberParser()

dataBase = Database()
dataBase.insert({
    "name": "Ripan",
    "email": "email",
    "phoneNumber": "559754982",
    "aboutMe": "I am Ripan",
    "education": "San Jose State",
    "projects": "Easyy Link",
    "skills": "c++",
    "experience": "Spotlyt"
})
dataBase.getUser(3)


