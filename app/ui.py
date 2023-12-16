try:
	from Tkinter import *
except ModuleNotFoundError:
	from tkinter import *

# global variables
TEMP_HEIGHT = 50
TEMP_WIDTH = 30

SYMBOL_CROSS = 10007 # ballot symbol
SYMBOL_CHECK = 10003 # check mark symbol

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
		self.columnconfigure(0, weight=2)
		self.columnconfigure(1, weight=2)

		self.rowconfigure(0, weight=2)
		self.rowconfigure(1, weight=1)

		# setting up frames
		self.medicines_frame = MedicinesFrame(self)
		self.medicines_frame.initialize()
		self.medicines_frame.grid(row=0, column=0, sticky="nsew", rowspan=2)

		self.details_frame = DetailsFrame(self)
		self.details_frame.initialize()
		self.details_frame.grid(row=0, column=1, sticky="nsew")

		self.buttons_frame = ButtonsFrame(self)
		self.buttons_frame.initialize()
		self.buttons_frame.grid(row=1, column=1, sticky="nsew")

		self.frames = self.winfo_children()


	# add new medicine to UI
	def add_new_medicine(self, id_value, name_value):
		self.medicines_frame.new_label(id_value, name_value)


"""Frames"""
# color_palette = ['bg_color', 'fg_color', dark_bg_color, dark_fg_color]

# labels
class MedicinesFrame(Frame):
	
	color_palette = ['lime', 'white', 'grey', 'white']

	def __init__(self, parent):
		Frame.__init__(self, parent, bg = MedicinesFrame.color_palette[0])

		# arrange elements
		self.next_row = 1

		print("Added: MedicinesFrame")

	def initialize(self):
		self.grid()
		
		# configuring columns and rows
		self.columnconfigure(0, weight=1)

		# elements
		self.heading = Label(self, text="Medicines", bg=MedicinesFrame.color_palette[0])
		self.heading.grid(row=0, column=0, columnspan=2, sticky="ew")

	def new_label(self, id_value, name_value):
		temp = Label(self, text=name_value, bg=MedicinesFrame.color_palette[0])
		temp.grid(row=self.next_row, column=0, sticky="ew")
		
		temp.bind("<Enter>", func=lambda e: temp.config(
        background=MedicinesFrame.color_palette[2]))

		temp.bind("<Leave>", func=lambda e: temp.config(
        background=MedicinesFrame.color_palette[0]))

		self.next_row+=1


# entry boxes
class DetailsFrame(Frame):
	
	color_palette = ['orange', 'red', 'grey', 'white']
	
	def __init__(self, parent):
		Frame.__init__(self, parent, bg = DetailsFrame.color_palette[0])
		print("Added: DetailsFrame")

	def initialize(self):
		self.grid()
		
		# configuring columns and rows
		self.columnconfigure(0, weight=1)
		self.columnconfigure(1, weight=1)

		# elements
		self.heading = Label(self, text="Details")
		self.heading.grid(row=0, column=0, columnspan=2, sticky="ew")
		
		self.sl_no_entry = Entry(self)
		self.sl_no_entry.grid(row=1, column=0, sticky="ew")

		self.name_entry = Entry(self)
		self.name_entry.grid(row=1, column=1, sticky="ew")

		self.desc_entry = Entry(self)
		self.desc_entry.grid(row=2, column=0, rowspan=2, sticky="nsew")

		self.duration_entry = Entry(self)
		self.duration_entry.grid(row=2, column=1, sticky="ew")

		self.streak_entry = Entry(self)
		self.streak_entry.grid(row=3, column=1, sticky="ew")

# buttons
class ButtonsFrame(Frame):
	
	color_palette = ['cyan', 'darkblue', 'grey', 'white']
	
	def __init__(self, parent):
		Frame.__init__(self, parent, bg = ButtonsFrame.color_palette[0])
		print("Added: ButtonsFrame")

	def initialize(self):
		self.grid()
		
		# configuring columns and rows
		self.columnconfigure(0, weight=1)
		self.columnconfigure(1, weight=1)

		# elements
		self.btn_1 = Button(self, text = chr(SYMBOL_CROSS))
		self.btn_1.grid(row=1, column=0, sticky="new")

		self.btn_2 = Button(self, text = chr(SYMBOL_CHECK))
		self.btn_2.grid(row=2, column=0, sticky="ews")

if __name__ == '__main__':
	myapp = App(None)
	myapp.title("Medicine Tracker")
	myapp.geometry("500x500")
	myapp.mainloop()