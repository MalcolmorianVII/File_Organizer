from tkinter import *
from Organizer import *
from tkinter import ttk
from functools import partial


def check():
    var_value = var.get()
    if var_value == "All":
        all()
    elif var_value == "Audios":
        auds(aud_files)
    elif var_value == "Videos":
        vids(vid_files)
    else:
        docs(doc_files)


root = Tk()
var = StringVar(root, "1")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

default_button = Radiobutton(mainframe, text="default", variable=var, value="Default")
default_button.grid(column=5,row=2,sticky=(W,E))
custom_button = Radiobutton(mainframe, text="custom", variable=var, value="Custom")
custom_button.grid(column=5,row=4,sticky=(W,E))
# var = StringVar(root, "1")
# R1 = Radiobutton(root, text="All", variable=var, value="All")
# R1.pack(anchor=W)
#
# R2 = Radiobutton(root, text="Audios", variable=var, value="Audios")
# R2.pack(anchor=W)
#
# R3 = Radiobutton(root, text="Videos", variable=var, value="Videos")
# R3.pack(anchor=W)
#
# R4 = Radiobutton(root, text="Documents", variable=var, value="Docs")
# R4.pack(anchor=W)


# code engine & GUI linkage
# Organize = Button(root, text="Organize", command=check)
# Organize.pack(anchor=W)

root.mainloop()
