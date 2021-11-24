import sqlite3
from pathlib import Path

Path('user.db').touch()

#connection
conn = sqlite3.connect('user.db')
c = conn.cursor()

SQL_CreateTable = '''CREATE TABLE IF NOT EXISTS user (
             user_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
             name TEXT NOT NULL,
             email TEXT NOT NULL,
             phoneNumber TEXT NOT NULL,
             title TEXT NOT NULL,
             education TEXT NOT NULL,
             projects TEXT NOT NULL,
             skills TEXT NOT NULL,
             experience TEXT NOT NULL
             )'''
             
c.execute(SQL_CreateTable)