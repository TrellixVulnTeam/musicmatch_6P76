
import sqlite3
import json
from unittest import result
from colorama import Cursor

#from django.db import connection

#define connection and cursor

connection = sqlite3.connect('songs.db')

Cursor = connection.cursor()

#creating song table for spotify songs

command1 = """CREATE TABLE IF NOT EXISTS
youtube(name TEXT,)"""

Cursor.execute(command1)

#adding data to song table

Cursor.execute("INSERT INTO songs VALUES ('Better')")


connection.commit()


Cursor .execute("SELECT * FROM youtube")

results = Cursor.fetchall()
print(results)
