from tkinter import *
from PIL import ImageTk,Image

# evokens Tk()
root = Tk()
#root title
root.title("FRAME")
#root icon
root.iconbitmap("icon.ico")


frame = LabelFrame(root, padx=50, pady=50)
frame.pack(padx=10, pady=10)

b = Button(frame, text="Don't Click Here!")
b2 = Button(frame, text="...or here!")
b.grid(row=0, column=0)
b2.grid(row=1, column=1)




root.mainloop()