import sqlite3
import sys

def printDB():
    try:
        result = theCursor.execute("SELECT ID, FName, LName, Age, Address, Salary, HireDate FROM Employees")

        for row in result:
            print("ID :", row[0])
            print("FName :", row[1])
            print("LName :", row[2])
            print("Age :", row[3])
            print("Address :", row[4])
            print("Salary :", row[5])
            print("HireDate :", row[6])

    except sqlite3.OperationalError:
        print("Table does not exist")

    except:
        print("Could not retrieve data from database")

def updateDB():
    try:
        db_conn.execute("UPDATE Employees SET Address = '345 Ketu Lagos' WHERE ID=1")
        db_conn.commit()
    except sqlite3.OperationalError:
        print("Table could not be updated")

def deleteDB():
    try:
        db_conn.execute("DELETE FROM Employees WHERE ID=1")
        db_conn.commit()

    except sqlite3.OperationalError:
        print("Table could not be deleted")


def alterDataInTable():
    try:
        db_conn.execute("ALTER TABLE Employees ADD COLUMN 'Image' BLOB DEFAULT NULL")
        db_conn.commit()
    except sqlite3.OperationalError:
        print("Table could not be altered")

db_conn = sqlite3.connect('test.db')

print("Database connection established")

theCursor = db_conn.cursor()

db_conn.execute("DROP TABLE IF EXISTS Employees")
db_conn.commit()

try:
    db_conn.execute("CREATE TABLE Employees(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, FName TEXT NOT NULL, LName TEXT NOT NULL, Age INTEGER NOT NULL, Address TEXT, Salary REAL, HireDate TEXT);")
    db_conn.commit()
    
except sqlite3.OperationalError:
    print("table could not be created")


db_conn.execute("INSERT INTO Employees (FName, LName, Age, Address, Salary, HireDate) VALUES ('Joshua', 'Alana', 17, '1234 Main street', 500000, date('now'))")
db_conn.commit()


printDB()
updateDB()
printDB()
deleteDB()
printDB()
alterDataInTable()


theCursor.execute("PRAGMA TABLE_INFOR(Employees)")

rowNames = [nameTuple[1] for nameTuple in theCursor.fetchall()]

print(rowNames)

theCursor.execute("SELECT COUNT(*) FROM Employees")

numOfRows = theCursor.fetchall()
print(numOfRows)

theCursor.execute("SELECT SQLITE_VERSION()")
print("SQlite Version :", theCursor.fetchone())

db_conn.rollback()

# writing information into a temporary file
with open('dump.sql', 'w') as f:
    for line in db_conn.iterdump():
        f.write("%s\n" % line)

print("Table created successfully")
db_conn.close()

print("Database connection closed")