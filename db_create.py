__author__ = 'davidfreer'
import sqlite3
from _config import DATABASE_PATH
with sqlite3.connect(DATABASE_PATH) as connection:
    c = connection.cursor()
    c.execute("""CREATE TABLE tasks(task_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, due_date TEXT NOT
              NULL, priority INTEGER NOT NULL, status INTEGER NOT NULL)""")
    c.execute('INSERT INTO tasks (name, due_date, priority, status)'
              'VALUES("Finish this tutorial", "3/25/2015",10,1)')
    c.execute('INSERT INTO tasks (name, due_date, priority, status)'
              'VALUES("Have fun!", "6/25/2015",10,1)')