import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
root.title("App_runner")
apps = []

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempapps = f.read()
        tempapps = tempapps.split(',')
        apps = [x for x in tempapps if x.strip()]


def addapp():
    for widget in frame.winfo_children():
        widget.destroy()
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="select a file",
                                          filetypes=(("executables", "*exe"),
                                                     ("all files", "*.*")))
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack(pady=5)


def runapps():
    for app in apps:
        os.startfile(app)


canvas = tk.Canvas(root, height=500, width=500, bg="#fcb41f")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relheight=0.8, relwidth=0.8, relx=0.1, rely=0.1)

openfile = tk.Button(root,
                     text="openfile",
                     padx=10,
                     pady=5,
                     fg="black",
                     bg="#fcb41f",
                     command=addapp)
openfile.place(relheight=0.1, relwidth=0.2, relx=0.4, rely=0.6)

runapps = tk.Button(root,
                    text="run apps",
                    padx=10,
                    pady=5,
                    fg="black",
                    bg="#fcb41f",
                    command=runapps)
runapps.place(relheight=0.1, relwidth=0.2, relx=0.4, rely=0.7)

for apps in apps:
    label = tk.Label(frame, text=apps)
    label.pack()

root.mainloop()

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')