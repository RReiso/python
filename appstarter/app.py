import tkinter as tk
# filedialog - to pick apps, Text - to display text
from tkinter import filedialog, Text
import subprocess
import sys
import os

root = tk.Tk()  # the frame of the app
apps = []


# if file save.txt exists:
if os.path.isfile("save.txt"):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(",")
        # return x if ... (like filter in JS?)
        apps = [x for x in tempApps if x.strip()]
        print(apps)


# opens a filesearch box, starts at the initialdir folder, show what files can be chosen
def addApp():
    # remove all labels
    for widget in frame.winfo_children():  # references frame from line 51
        widget.destroy()

    filename = filedialog.askopenfilename(
        initialdir="/home", title="Select your file", filetypes=(("executables", "*.exe"), ("all files", "*.*")))
    apps.append(filename)
    print(filename)
    for app in apps:
        # add labels
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()


def runApps():
    # for Linux and Macos
    for app in apps:
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, app])


# attach canvas to root
canvas = tk.Canvas(root, height=700, width=700,
                   bg="#263D42")
canvas.pack()

# add another box in the canvas
frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

# add a button
openFile = tk.Button(root, text="Open File :)", padx=10,
                     pady=5, fg="white", bg="#263D42", command=addApp)
openFile.pack()
runApps = tk.Button(root, text="Run my apps :)", padx=10,
                    pady=5, fg="white", bg="#263D42", command=runApps)
runApps.pack()

for app in apps:
    # add labels
    label = tk.Label(frame, text=app, bg="gray")
    label.pack()

root.mainloop()  # opens a gui box

# save apps to a file
with open("./save.txt", "w") as f:
    for app in apps:
        f.write(app + ",")
