#Parser class to read a pdf file and parse resume fields
import re #reg ex
from pdfminer.high_level import extract_text #to extract text from resume

class Parser:
    
    #constructor: takes a path to resume file
    def __init__(self, fileName):
        self.__resume_string = extract_text(f'./static/uploads/{fileName}')

    #parse phone number from file
    def phoneNumberParser(self):
        pattern = re.compile(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')
        match = re.findall(pattern, self.__resume_string)
        if match:
            return match[0]
        else:
            return "None"
    
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
            newResStr = self.__resume_string.replace("\n", " ")
            pattern2 = re.compile(r'(EDUCATION.*|Education.*)(SKILLS & HONOR|SKILLS AND TECHNOLOGIES|Skills|PROJECTS|Projects|EXPERIENCE|SKILLS|Experience)')
            match2 = re.findall(pattern2, newResStr)
            result2 = ""
            if match2:
                result2 = result2 + match2[0][0] + '\n'
                return result2
            else:
                return "None"
    
    #parser projects
    def projectsParser(self):
        newResStr = self.__resume_string.replace("\n", " ")
        pattern = re.compile(r'(PROJECTS.*|Projects.*)(SKILLS & HONOR|Skills|Education|Experience|EXPERIENCE)')
        match = re.findall(pattern, newResStr)
        result = ""
        if match:
            result = result + match[0][0] + '\n'
            return result
        else:
            return "None"

    #parser for experience
    def experienceParser(self):
        newResStr = self.__resume_string.replace("\n", " ")
        pattern = re.compile(r'(EXPERIENCE.*|Experience.*|Work.*)(PROJECTS|Projects|Skills|SKILLS & HONOR|SKILLS|Education|EDUCATION)')
        match = re.findall(pattern, newResStr)
        result = ""
        if match:
            result = result + match[0][0] + '\n'
            return result
        else:
            return "None"

    #parser for skills
    def skillParser(self):
        skills = []
        with open("./static/uploads/skills_text", "r") as file:
            for line in file.readlines():
                skills.append(line.strip())

        skills_string = ""
        res = self.__resume_string.split()
        
        for ele in res:
            if ele in skills:
                skills_string = skills_string + ele + ", "
        
        return skills_string