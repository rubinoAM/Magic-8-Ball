# Imports
from eightball import *
import tkinter as tk

# TKinter
root = tk.Tk()
ball = tk.PhotoImage(file="eightball.gif")

w1 = tk.Label(root, image=ball).pack(side="right")
w2 = tk.Label(root,justify=tk.LEFT,text="Lay It Down! Lay It Down!").pack(side="left")

root.mainloop()

"""mjg = Eightball()
print(mjg.roll())"""