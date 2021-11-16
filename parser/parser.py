import re
from pdfminer.high_level import extract_text

class Parser:
    
    #constructor: takes a path to resume file
    def __init__(self, fileName):
        self.__resume_string = extract_text(f'./static/uploads/{fileName}')
        #self.__resume_string = extract_text('../static/uploads/RipandeepSinghResumeCurrent_1.pdf')

    #parse phone number from file
    def phoneNumberParser(self):
        pattern = re.compile(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]')
        match = re.findall(pattern, self.__resume_string)
        if match:
            return match[0]
        else:
            return None
    
    #parse school name from file
    def schoolParser(self):
        pattern = re.compile(r'(Bachelor.*|Associate.*|BS.*|AS.*|Masters.*)')
        match = re.findall(pattern, self.__resume_string)
        result = ""
        if match:
            for m in match:
                result = result + m + '\n'
            return result
        else:
            return None
    
    #parser projects
    def projectsParser(self):
        if "PROJECTS" in self.__resume_string:
            ind = self.__resume_string("PROJECTS")
            
        pattern = re.compile(r'(Projects.*|PROJECTS.*)')
        match = re.findall(pattern, self.__resume_string)
        result = ""
        if match:
            for m in match:
                result = result + m + '\n'
            return result
        else:
            return None
#parser = Parser("RipandeepSinghResumeCurrent_1.pdf")
#print(parser.projectsParser())