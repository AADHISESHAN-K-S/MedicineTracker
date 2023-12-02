try:
	from Tkinter import *
except ModuleNotFoundError:
	from tkinter import *


def main():
	root = Tk()
	root.title("Medicine Tracker")
	
	# configuring columns
	# root.columnconfigure(0, weight=1)
	# root.columnconfigure(1, weight=1)

	# frames
	medicines_frame = Frame(root)
	medicines_frame.grid(row=0, column=0)

	details_frame = Frame(root)
	details_frame.grid(row=0, column=1)

	buttons_frame = Frame(root)
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

	
	root.mainloop()

if __name__ == '__main__':
	main()