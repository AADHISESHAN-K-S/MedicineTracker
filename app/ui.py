try:
	from Tkinter import *
except ModuleNotFoundError:
	from tkinter import *


class App(Tk):
	def __init__(self, parent):
		Tk.__init__(self, parent)
		self.parent = parent
		# self.frames = []
		self.initialize()

	def initialize(self):
		
		self.grid()

		# configuring columns
		self.columnconfigure(0, weight=1)
		self.columnconfigure(1, weight=1)

		# configuring rows
		self.rowconfigure(0, weight=1)
		self.rowconfigure(1, weight=1)

		# frames
		medicines_frame = Frame(self)
		medicines_frame.grid(row=0, column=0)

		details_frame = Frame(self)
		details_frame.grid(row=0, column=1)

		buttons_frame = Frame(self)
		buttons_frame.grid(row=1, column=1)

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

		# entry boxes
		sl_no_entry = Entry(details_frame)
		sl_no_entry.grid(row=0, column=0)

		name_entry = Entry(details_frame)
		name_entry.grid(row=0, column=1)

		desc_entry = Entry(details_frame)
		desc_entry.grid(row=1, column=0, rowspan=2)

		duration_entry = Entry(details_frame)
		duration_entry.grid(row=1, column=1)

		streak_entry = Entry(details_frame)
		streak_entry.grid(row=2, column=1)

		# buttons
		add_btn = Button(buttons_frame, text = "ADD")
		add_btn.grid(row=0, column=0)

		del_btn = Button(buttons_frame, text = "DELETE")
		del_btn.grid(row=0, column=1)

		take_btn = Button(buttons_frame, text = "TAKE")
		take_btn.grid(row=1, columnspan=2)

		miss_btn = Button(buttons_frame, text = "MISS")
		miss_btn.grid(row=2, columnspan=2)


		# self.frames = self.winfo_children()

		# run on resize
		self.bind("<Configure>", self.on_resize)

	# scale the font size of widgets upon window resize
	def on_resize(self, event):
		new_width = event.width
		new_height = event.height

		new_font_size = max(int(new_width/20), 13)

		new_font = ("Arial", new_font_size)

		""" optimize """
		for frame in self.winfo_children():
			for widget in frame.winfo_children():
				# print(widget)
				widget.configure(font=new_font)

		# debugging
		# print(f"Window: {new_width}x{new_height}, font_size = {new_font_size}")

if __name__ == '__main__':
	myapp = App(None)
	myapp.title("Medicine Tracker")
	myapp.mainloop()