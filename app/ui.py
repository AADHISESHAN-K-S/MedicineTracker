try:
	from Tkinter import *
except ModuleNotFoundError:
	from tkinter import *


def main():
	root = Tk()
	root.title("Medicine Tracker")
	root.mainloop()

if __name__ == '__main__':
	main()