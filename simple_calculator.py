from tkinter import *

class App(TK):
	def __init__(self):
		self.root = Tk()
		self.root.title("BMI Calculator")



		#Sets a label and entry field
		self.label = label(self.root, text = "Enter yourt weight in kolograms.").pack()
		self.weight = StringVar()
		Entry(self.root, textvariable = self.weight.pack())
		self.label = Label(self.root text = "enter your height in meters").pack()
		self.height = StringVar()
		Entry(self.root, textvariable= self.height).pack()

		self.buttontext = StringVar()
		Button(self.root, textvariable = self.buttontext, commnad = self.calculate).pack()
		self.buttontext.set("Calculate")

		self.bmi_num = StringVar()
		Label(self.root, textvariable= self.bmi_num).pack()

		self.bmi_text = Stringvar()

		self.root.mainloop()

	def calculate(self):

		weight = float(self.weight.get())
		height = float(self.height.get())
		bmi = float((weight)/(height**2))

		"""self.bmi_num.set("your BM is %.2f" % bmi)
								if bmi<18.5:
									self.bmi_text.set("You are underweight")
								if 18"""

App()