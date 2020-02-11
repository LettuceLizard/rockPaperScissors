#tkinter gui
import tkinter as tk
from random import randint
"""
rps = rock paper scissors
master = root window
"""
class mainWindow():
	def __init__(self, master, rps, width=400, height=400):
		self.master = master
		self.canvas = tk.Canvas(master, width=width, height=height)
		
		"""pack"""
		self.canvas.pack()

	def createRectangle(self, posXY):
		self.canvas.create_rectangle


class rockPaperScissors():
	def __init__(self):
		self.player1 = ""
		self.player2 = ""
		self.choices = ("paper", "rock", "scissors")

	def setChoice(self, string, player1=True):
		if string in self.choices:
			if player1 == True:
				self.player1 = string
			else:
				self.player2 = string
		else: return False


	def setRandomValue(self, player_2=True):
		if player_2 == True:
			self.player2 = self.choices[randint(0, 2)]
		else:
			self.player1 = self.choices[randint(0, 2)]

	def getWinner(self):
		""" get winner returns: (None = draw, True = player1 wins,
		False = player2 wins)
		"""
		if self.player1 == self.player2:
			winner = None
		else:
			winner = self.Didplayer1Win(self.player1, self.player2)
		return winner


	def Didplayer1Win(self, player1Choice, player2Choice):
		#returnerar om player1 är vinnare(True) eller False
		results = {
		("rock", "scissors"):True,
		("paper", "rock"):True,
		("scissors", "paper"):True,
		("scissors", "rock"):False,
		("rock", "paper"):False,
		("paper", "scissors"):False,
		}
		return results[(player1Choice, player2Choice)]






def main():
	root = tk.Tk()
	rpsLogic = rockPaperScissors()
	app = mainWindow(root)
	root.mainloop()

if __name__ == '__main__':
	main()

"""testa classerna"""
testRPS = rockPaperScissors()
testRPS.setChoice("paper")
testRPS.setRandomValue()
print(testRPS.player2)
print(f"player1 wins = {testRPS.getWinner()}")
