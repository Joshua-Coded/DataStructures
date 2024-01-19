import sqlite3
import sys

db_conn = sqlite3.connect('test.db')

print("Database connection established")

theCursor = db_conn.cursor()

db_conn.execute("DROP TABLE IF EXISTS Employees")
db_conn.commit()

try:
    db_conn.execute("CREATE TABLE Employees(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, FName TEXT NOT NULL, LName TEXT NOT NULL, Address TEXT, Salary REAL, HireDate TEXT);")
    db_conn.commit()
    
except sqlite3.OperationalError:
    print("table could not be created")

print("Table created successfully")
db_conn.close()

print("Database connection closed")