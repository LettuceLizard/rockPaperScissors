#tkinter gui
import tkinter as tk

class mainWindow():
	def __init__(self, master, width=400, height=400):
		self.master = master



def main():
	root = tk.Tk()
	app = mainWindow(root)
	root.mainloop()

if __name__ == '__main__':
	main()