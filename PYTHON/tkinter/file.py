from tkinter import *
from tkinter import ttk

root = Tk()

# root.title("First GUI")

# ttk.Button(root, text="Hello Joshua").grid()

# frame = Frame(root)

# labelText = StringVar()

# label = Label(frame, textvariable=labelText)
# button = Button(frame, text="Click Me")

# labelText.set("I am a Developer")

# label.pack()
# button.pack()
# frame.pack()

# Label(frame, text="A Bunch of awesome Buttons").pack()

# Button(frame, text="Button 1").pack(side=LEFT, fill=Y)
# Button(frame, text="Button 2").pack(side=TOP, fill=X)
# Button(frame, text="Button 3").pack(side=RIGHT, fill=X)
# Button(frame, text="Button 4").pack(side=LEFT, fill=X)

# frame.pack()

Label(root, text="First Name:").grid(row=0, sticky=W, padx=4)
Entry(root).grid(row=0, column=1, sticky=E, pady=4)


Label(root, text="Last Name:").grid(row=1, sticky=W, padx=4)
Entry(root).grid(row=1, column=1, sticky=E, pady=4)

Button(root, text="Submit").grid(row=3)
root.mainloop()