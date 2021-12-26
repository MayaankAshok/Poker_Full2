from Poker_Final.Interface.MonteCarloReturn import run_MonteCarlo
import pyautogui as pag
import PIL.ImageGrab


BUTTON_FOLD =(1984,1568)
BUTTON_CHECK = (2236,1569)
BUTTON_CALL = (2488,1568)
BUTTON_RAISE = (2399,1643)
BUTTON_ALLIN= (2391,1728)
SLIDER_RAISE = ((1819,1713),2224,1715)

FLOP_1 =((1343,965),(1432,1076))
FLOP_2  =((1453,962),(1542,1080))
FLOP_3 =((1561,960),(1652,1078))
HAND_1 =((1419,1534),(1548,1703))
HAND_2 = ((1574,1535),(1708,1702))

class Player:
	def __init__(self):
		self.chips = 0
		self.hand = []
		self.status = 0
		self.raiseAmount = 0


class Table:
	def __init__(self):
		self.bets = (0, 0)
		self.activeAmount = 0
		self.activePot = 0
		self.totalPot  = 0
		self.cards = [[], [], []]

	def readTable(self):
		cardH1 = PIL.ImageGrab.grab(bbox=HAND_1[0]+HAND_1[1])
		cardH2 = PIL.ImageGrab.grab(bbox=HAND_2[0] + HAND_2[1])
		cardF1 = PIL.ImageGrab.grab(bbox=FLOP_1[0]+FLOP_1[1])
		cardH2 = PIL.ImageGrab.grab(bbox=FLOP_2[0] + FLOP_2[1])
		cardH3 = PIL.ImageGrab.grab(bbox=FLOP_3[0] + FLOP_3[1])
		cardT = PIL.ImageGrab.grab(bbox=HAND_1[0] +  [1])
		cardR = PIL.ImageGrab.grab(bbox=HAND_1[0] + HAND_1[1])

class Game:
	def __init__(self):
		self.numOpponents = 2
		self.playerList = []
		self.setupPlayers()
		self.table = Table()

	def setupPlayers(self):
		self.playerList = [Player() for _ in range(self.numOpponents)]


class ActivePlayer(Player):
	def __init__(self):
		super().__init__()
		self.game = Game()

	def makeDecision(self):
		winList = run_MonteCarlo([self.hand]+self.game.table.cards , opponents=self.game.numOpponents)
		winNorm = (winList[0]+winList[2])*self.game.numOpponents*100/(winList[1]+winList[2])
		if winNorm >= 50:
			if winNorm <= 175:
				self.Call()
			else:
				self.Raise()
		else:
			self.Check_Fold()

	def Call(self):
		if self.chips >= self.game.table.activeAmount:
			self.game.table.activePot += self.game.table.activeAmount
			self.chips -= self.game.table.activeAmount
			self.actCall()
		else:
			self.game.table.activePot += self.chips
			self.chips = 0
			self.actAllIn()

	def Check_Fold(self):
		if self.game.table.activeAmount > 0:
			self.actFold()

		else:
			self.actFold()

	def Raise(self):
		if self.chips >= 2 * self.game.table.activeAmount:

			self.game.table.pot += 2 * self.game.table.activeAmount
			self.game.table.activeAmount *= 2
			self.actRaise(self.game.table.activeAmount)
			self.chips -= self.game.table.activeAmount
		else:
			if self.game.table.activeAmount < self.chips:
				self.game.table.activeAmount = self.chips
				self.game.table.activePot += self.chips
				self.actRaiseAllIn()
				self.chips = 0

			else:

				self.game.table.activePot += self.chips
				self.actRaiseAllIn()
				self.chips = 0

	def actCheck(self):
		pag.click(BUTTON_CHECK[0],BUTTON_CHECK[1])

	def actCall(self):
		pag.click(BUTTON_CALL[0],BUTTON_CALL[1])

	def actFold(self):
		pag.click(BUTTON_FOLD[0],BUTTON_FOLD[1])

	def actRaiseAllIn(self):
		pag.click(BUTTON_ALLIN[0],BUTTON_ALLIN[1])

	def actRaise(self,amount):
		pass

	def actAllIn(self):
		pass

print("done")
