# Imports
from eightball import *
import tkinter as tk

# TKinter
root = tk.Tk()
root.title('Magic Eight Ball')

win_x = int(root.winfo_screenwidth()/2 - root.winfo_reqwidth()/2)
win_y = int(root.winfo_screenheight()/2 - root.winfo_reqheight()/2)

root.geometry("550x400+{}+{}".format(win_x, win_y))

start_text = "Ah, yes. The old magic eight ball!\nLet's dust this sucker off and give a quick shake, shall we?"
start_msg = tk.Message(root, text=start_text)
start_msg.config(bg='chartreuse',font=('Helvetica',24,"bold"))
start_msg.pack()

#ball = tk.PhotoImage(file="eightball.gif")
#w = tk.Label(root, image=ball).pack()

root.mainloop()

"""mjg = Eightball()
print(mjg.roll())"""