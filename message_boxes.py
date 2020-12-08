from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
# evokens Tk()
root = Tk()
#root title
root.title("Radio-Buttons")
#root icon
root.iconbitmap("icon.ico")

def popup():
	messagebox.showinfo("This is my pop up", "This is below")



Button(root, text = "Click me!", command = popup).pack()
















root.mainloop()
