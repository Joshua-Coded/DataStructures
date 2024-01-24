from tkinter import *
from tkinter import ttk
import sqlite3

class StudentDB:

    # Class Field
    db_conn = 0
    theCursor = 0
    curr_student = 0
    
    def setup_db(self):

        # Open or create database
        self.db_conn = sqlite3.connect('student.db')

        # create cursor
        self.theCursor = self.db_conn.cursor()
        try: 
            # create table if it doesn't exist
            self.db_conn.execute("CREATE TABLE IF NOT EXISTS Students(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, FName TEXT NOT NULL, LName TEXT NOT NULL);")

            self.db_conn.commit()
        except sqlite3.OperationalError:
            print("ERROR: TABLE NOT CREATED")

    def student_submit(self):
        # Insert Students into database
        self.db_conn.execute("INSERT INTO Students(FName, LName)" + "VALUES('" + self.fn_entry_value.get() + "', '" +  self.ln_entry_value.get() + "')")
        
        # Clear Entry Boxes
        self.fn_entry.delete(0, "end")
        self.ln_entry.delete(0, "end")
        
        # Update List Box
        self.update_listbox()

        # Delete items in list Box
       
    def update_listbox(self):
        self.list_box.delete(0, "end")

        # Get the student from the db
        try:
            result = self.theCursor.execute("SELECT ID, FName, LName FROM Students")
            for row in result:
                stud_id = row[0]
                stud_fname = row[1]
                stud_lname = row[2]

            # put students in the list box
                self.list_box.insert(stud_id, stud_fname + " " + stud_lname)
        except sqlite3.OperationalError:
            print("The Table Doesn't Exist")

        except:
            print("1: Couldn't Retrieve Data From Database")

    def load_student_list(self, event=None):
        # Get index of selected which is the student
        lb_widget = event.widget
        index = str(lb_widget.curselection()[0] + 1)

        # Store the current student index 
        self.curr_student_index = index
        
        # Retrieve the student list from database
        try:
            result = self.theCursor.execute("SELECT ID, FName, LName FROM Students WHERE ID=" + index)

            for row in result:
                stud_id = row[0]
                stud_fname = row[1]
                stud_lname = row[2]
        # set the names in the entries.
                self.fn_entry_value.set(stud_fname)
                self.ln_entry_value.set(stud_lname)

        except sqlite3.OperationalError:
            print("Could not get student list from database")
        except:
            print("1: the list was empty")


    def student_update(self):
        # Update based on the current student
        try:
            self.db_conn.execute("UPDATE Students SET FName='" + self.fn_entry_value.get() + "', LName='" + self.fn_entry_value.get() +" ' WHERE ID=" + self.curr_student)

            self.db_conn.commit()

        except sqlite3.OperationalError:
            print("Could not update student list from database")

        # clear entries
        self.fn_entry.delete(0, "end")
        self.ln_entry.delete(0, "end")

        # update the list of students
        self.update_listbox()

    def __init__(self, root):
        root.title("Student Database")
        root.geometry("300x350")

        #--------- First Row ------------
        fn_label = Label(root, text="First Name")
        fn_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        self.fn_entry_value = StringVar(root, value="")
        self.fn_entry = ttk.Entry(root, textvariable=self.fn_entry_value)

        self.fn_entry.grid(row=0, column=1, padx=10, pady=10, sticky=W)

        # ------- Second Row --------------------------------
        ln_label = Label(root, text="Second Name")
        ln_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)

        self.ln_entry_value = StringVar(root, value="")
        self.ln_entry = ttk.Entry(root, textvariable=self.ln_entry_value)
        self.ln_entry.grid(row=1, column=1, padx=10, pady=10, sticky=W)


        # ---- 3rd Row -----------------
        self.submit_button = ttk.Button(root, text="Submit", command=lambda: self.student_submit())
        self.submit_button.grid(row=2, column=0, padx=10, pady=10, sticky=W)
           
        # ---- 4th Row -----------------
        self.update_button = ttk.Button(root, text="Update", command=lambda: self.student_update())
        self.update_button.grid(row=2, column=1, padx=10, pady=10)

        # 5th Row ----------------
        scrollbar = Scrollbar(root)

        self.list_box = Listbox(root)

        self.list_box.bind('<<ListBoxSelect>>', self.load_student_list)

        self.list_box.insert(1, "Students Here")

        self.list_box.grid(row=3, column=0, columnspan=4, padx=10, pady=10, sticky=W+E)

        # call the database creation
        # self.setup_db()

        # self.update_listbox()

root = Tk()
studDB = StudentDB(root)

root.mainloop()