"""core.py"""
# medicine2 = Medicine('newMed2', 'test2', 24, 3)
# medicine3 = Medicine('newMed3', 'test3', 34, 3)
# medicine4 = Medicine('newMed4', 'test4', 44, 3)

# print(medicine1.remaining)
# print(medicine2.remaining)
# print(medicine3.remaining)
# print(medicine4.remaining)


"""ui.py"""
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