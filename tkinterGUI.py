#tkinter gui
import tkinter as tk
from random import randint

class mainWindow():
	def __init__(self, master, width=400, height=400):
		self.master = master
		self.canvas = tk.Canvas(master, width=width, height=height)
		
		"""pack"""
		self.canvas.pack()

	def createRectangle(self, posXY):
		self.canvas.create_rectangle


class rockPaperScissors():
	def __init__(self):
		self.player1 = None
		self.player2 = None
		self.choices = ("paper", "rock", "scissors")

	def setChoice(self, string, player1=True):
		if string in self.choices:
			if player1 == True:
				self.player1 = string
			else:
				self.player2 = string
		else: return False


	def setRandomValue(self, player2=True):
		rock_paper_scissors = self.choices[randint(0, 2)]
		if player2 == True:
			self.player2 = rockPaperScissors
		else:
			self.player1 = rock_paper_scissors

	def getWinner(self):
		""" get winner returns: (None = draw, True = player1 wins,
		False = player2 wins)
		"""
		if self.player1 == self.player2:
			winner = None
		else:
			winner = Didplayer1Win(self.player1, self.player2)
		return winner


	def Didplayer1Win(self, player1Choice, player2Choice):
		results = {
		("rock", "scissors"):True,
		("paper", "rock"):True,
		("scissors", "paper"):True,
		("scissors", "rock"):False,
		("rock", "paper"):False,
		("paper", "scissors"):False,
		}
		return results[(player1Choice, player2Choice)]






# def main():
	# root = tk.Tk()
	# app = mainWindow(root)
	# root.mainloop()

if __name__ == '__main__':
	pass
	# main()

"""testa classerna"""
testRPS = rockPaperScissors()
testRPS.setRandomValue()
print(testRPS.player2)
print(testRPS.setChoice("paper"))