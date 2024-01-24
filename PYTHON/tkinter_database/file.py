from tkinter import *
from tkinter import ttk
import sqlite3

class StudentDB:


    # Class Field
    db_conn = 0
    theCursor = 0
    curr_student = 0
    
    def setup_db(self):
        print("setting up database")

    def student_submit(self):
        print("student submission")

    def student_update(self):
        print("student listbox updated")


    def load_student_list(self):
        print("loading student list")

    def updated_student_list(self):
        print("student list updated")

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
        self.submit_button = ttk.Button(root, text="Submit", command=lambda self: self.student_submit())
        self.submit_button.grid(row=2, column=0, padx=10, pady=10, sticky=W)
           
        # ---- 4th Row -----------------
        self.update_button = ttk.Button(root, text="Update", command=lambda self: self.student_update())
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