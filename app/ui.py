try:
	from Tkinter import *
except ModuleNotFoundError:
	from tkinter import *

# global variables
TEMP_HEIGHT = 50
TEMP_WIDTH = 30

"""ROOT"""
class App(Tk):
	def __init__(self, parent):
		Tk.__init__(self, parent)
		self.parent = parent
		self.frames = []
		self.initialize()

	def initialize(self):
		self.grid()

		# configuring columns and rows
		self.columnconfigure(0, weight=1)
		self.columnconfigure(1, weight=1)

		self.rowconfigure(0, weight=1)
		self.rowconfigure(1, weight=1)

		# setting up frames
		self.medicines_frame = MedicinesFrame(self)
		self.medicines_frame.initialize()
		self.medicines_frame.grid(row=0, column=0)

		self.details_frame = DetailsFrame(self)
		self.details_frame.initialize()
		self.details_frame.grid(row=0, column=1)

		self.buttons_frame = ButtonsFrame(self)
		self.buttons_frame.initialize()
		self.buttons_frame.grid(row=1, column=1)

		self.frames = self.winfo_children()


"""Frames"""
# labels
class MedicinesFrame(Frame):
	def __init__(self, parent):
		Frame.__init__(self, parent, bg = "lime")
		print("Added: MedicinesFrame")

	def initialize(self):
		self.grid()
		pass

# entry boxes
class DetailsFrame(Frame):
	def __init__(self, parent):
		Frame.__init__(self, parent, bg = "orange", height=TEMP_HEIGHT, width=TEMP_WIDTH)
		print("Added: DetailsFrame")

	def initialize(self):
		self.grid()

		self.sl_no_entry = Entry(self)
		self.sl_no_entry.grid(row=0, column=0)

		self.name_entry = Entry(self)
		self.name_entry.grid(row=0, column=1)

		self.desc_entry = Entry(self)
		self.desc_entry.grid(row=1, column=0, rowspan=2)

		self.duration_entry = Entry(self)
		self.duration_entry.grid(row=1, column=1)

		self.streak_entry = Entry(self)
		self.streak_entry.grid(row=2, column=1)


# buttons
class ButtonsFrame(Frame):
	def __init__(self, parent):
		Frame.__init__(self, parent, bg = "cyan")
		print("Added: ButtonsFrame")

	def initialize(self):
		self.grid()
		
		self.add_btn = Button(self, text = "ADD")
		self.add_btn.grid(row=0, column=0)

		self.del_btn = Button(self, text = "DELETE")
		self.del_btn.grid(row=0, column=1)

		self.take_btn = Button(self, text = "TAKE")
		self.take_btn.grid(row=1, columnspan=2)

		self.miss_btn = Button(self, text = "MISS")
		self.miss_btn.grid(row=2, columnspan=2)



if __name__ == '__main__':
	myapp = App(None)
	myapp.title("Medicine Tracker")
	myapp.geometry("500x500")
	myapp.mainloop()

"""later use"""
"""
		# scaling
		self.bind("<Configure>", self.on_resize)
	# scales the font size of widgets upon window resize
	def on_resize(self, event):
		new_width = event.width
		new_height = event.height

		new_font_size = max(int(new_width/20), 13)

		new_font = ("Arial", new_font_size)

		# **CHANGE TO ONLY AFFECT FRAMES** 
		for frame in self.winfo_children():
			for widget in frame.winfo_children():
				# print(widget)
				widget.configure(font=new_font)

		# debugging
		# print(f"Window: {new_width}x{new_height}, font_size = {new_font_size}")
	# appends new Label(medicine name) to medicines_frame
	def add_medicine(self, med_name):
		new_label = Label(self.medicines_frame, text=med_name)
		new_label.pack()
"""


"""
# labels
# (will be done automatically by a function that reads all the records)
placeholder_label1 = Label(medicines_frame, text="this is a medicine's name")
placeholder_label1.grid(row=0, column=0)

placeholder_label2 = Label(medicines_frame, text="this is a medicine's name")
placeholder_label2.grid(row=1, column=0)

placeholder_label3 = Label(medicines_frame, text="this is a medicine's name")
placeholder_label3.grid(row=2, column=0)

placeholder_label4 = Label(medicines_frame, text="this is a medicine's name")
placeholder_label4.grid(row=3, column=0)
"""