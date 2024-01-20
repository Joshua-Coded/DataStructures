from tkinter import *
from tkinter import ttk

root = Tk()

# root.title("First GUI")

# ttk.Button(root, text="Hello Joshua").grid()

frame = Frame(root)

labelText = StringVar()

label = Label(frame, textvariable=labelText)
button = Button(frame, text="Click Me")

labelText.set("I am a Developer")

label.pack()
button.pack()
frame.pack()

root.mainloop()