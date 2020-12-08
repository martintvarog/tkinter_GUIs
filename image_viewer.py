from tkinter import *
from PIL import ImageTk, Image


# evokens Tk()
root = Tk()
#root title
root.title("IMAGE VIEWER")
#root icon
root.iconbitmap("icon.ico")
root.geometry("400x400")




#open image
my_img1 = ImageTk.PhotoImage(Image.open("C:/Users/Jiří Kohout/Desktop/python_tkinter/random_pics/rand_1.jfif"))
my_img2 = ImageTk.PhotoImage(Image.open("C:/Users/Jiří Kohout/Desktop/python_tkinter/random_pics/rand_2.jfif"))
my_img3 = ImageTk.PhotoImage(Image.open("C:/Users/Jiří Kohout/Desktop/python_tkinter/random_pics/rand_3.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("C:/Users/Jiří Kohout/Desktop/python_tkinter/random_pics/sad_kitty.jpg"))

#list of images
image_list = [my_img1, my_img2, my_img3, my_img4]



#picks first image from list
my_label = Label(image = my_img1)
#position fir. imag. from list
my_label.grid(row = 0, column = 0, columnspan = 3)


status = Label(root, text= "Image 1 of " + str(len(image_list)), bd = 1, relief= SUNKEN)

#def back func
def back(image_number):
	global my_label
	global button_forward
	global button_back

	#forget previous image
	my_label.grid_forget()
	# show current image
	my_label = Label(image = image_list[image_number -1])
	#def of forward and back button
	button_forward = Button(root, text = ">>", command = lambda: forward(image_number + 1))
	button_back = Button(root, text = "<<", command = lambda: back(image_number - 1))

	#def of status bar 
	status = Label(root, text= "Image " + str(image_number) + " of " + str(len(image_list)), bd = 1, relief= SUNKEN)
	status.grid(row=2, column = 0, columnspan = 3, sticky= W + E)

	#disables when last pic 
	if image_number == 0:
		button_back= Button(root, text = "<<", state = DISABLED)

	#button position on scree
	my_label.grid(row = 0, column = 0, columnspan = 3)
	button_back.grid(row = 1, column = 0)
	button_forward.grid(row = 1, column = 2)

#def forw. func
def forward(image_number):
	global my_label
	global button_forward
	global button_back
	
	#forgets previous image
	my_label.grid_forget()
	#current image
	my_label = Label (image = image_list[image_number -1])
	#def of forw. backw. button
	button_forward = Button(root, text = ">>", command = lambda: forward(image_number + 1))
	button_back = Button(root, text = "<<", command = lambda: back(image_number - 1))

	#disables when last pic 
	if image_number == 3:
		button_forward = Button(root, text = ">>", state = DISABLED)

	#button position on scree
	my_label.grid(row = 0, column = 0, columnspan = 3)
	button_back.grid(row = 1, column = 0)
	button_forward.grid(row = 1, column = 2)

	#update status bar
	status = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN)
	status.grid(row=2, column=0, columnspan=3, sticky=W+E)



#button definition global
button_back = Button(root, text = "<<", command = lambda: back(1))
button_exit = Button(root, text = "EXIT PROGRAM", command = root.quit)
button_forward = Button(root, text = ">>", command = lambda: forward(2))
#button position global
button_back.grid(row = 1, column = 0)
button_exit.grid(row = 1, column = 1, pady = 10)
button_forward.grid(row = 1, column = 2)
status.grid(row=2, column = 0, columnspan = 3, sticky= W + E)











#never ending loop
root.mainloop()