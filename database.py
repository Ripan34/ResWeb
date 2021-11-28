import sqlite3

class Database:
    def __init__(self):
        self.__conn = sqlite3.connect('user.db')
        self.__c = self.__conn.cursor()
    
    #insert data
    def insert(self, data):
        self.__c.execute("INSERT INTO user VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (None, data["name"], data["email"], data["phoneNumber"],
        data["title"], data["education"], data["projects"], data["skills"], data["experience"], data["fileName"]))
        self.__conn.commit()
        return self.__c.lastrowid

    #get data
    def getUser(self, user_id):
        self.__c.execute("SELECT * FROM user WHERE user_id=:user_id", {"user_id": user_id})
        results = self.__c.fetchall() 
        return results
