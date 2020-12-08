from tkinter import *
from PIL import ImageTk,Image

# evokens Tk()
root = Tk()
#root title
root.title("Radio-Buttons")
#root icon
root.iconbitmap("icon.ico")

"""#saves r var
r = IntVar()
#sets default value of var r 
r.set("1")
"""
highlight = Label(root, text = "Pick your pizza").pack()
#MODES list, /w tuples 
MODES = [
	("hwa", "hwa"),
	("pepeornni", "pepeornni"),
	("oonio", "oonio"),
	("chillbill", "chillbill"),
]

pizza = StringVar()
pizza.set("chillbill")

for text, mode in MODES:
	Radiobutton(root, text= text, variable = pizza, value = mode).pack(anchor = W)

# returns picked value
def clicked(value):
	mylabel = Label(root, text = value)
	mylabel.pack()

# radiobutton deff + position
#Radiobutton(root, text= "Option 1", variable = r, value= 1, command = lambda: clicked(r.get())).pack()
#Radiobutton(root, text= "Option 2", variable = r, value= 2, command = lambda: clicked(r.get())).pack()
#default option label 
mylabel = Label(root, text = pizza.get()).pack( anchor = W)

#returns value of radiobutton
mybutton = Button(root, text = "click me!", command = lambda: clicked(pizza.get())).pack()


mybutton = Button(root, text= "Exit Programe", command = root.quit).pack()


root.mainloop()