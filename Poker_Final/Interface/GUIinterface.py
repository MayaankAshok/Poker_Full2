from .MonteCarloReturn import run_MonteCarlo
import sys
from PyQt5.QtCore import QThread, QObject
from PyQt5.QtWidgets import QApplication,QWidget ,QMainWindow , QPushButton,QLabel,QLineEdit,QGridLayout
import time

def parse_cards ( cardsIn: str ):
	cardList = cardsIn.split(" ")
	return [SUITS_TO_VAL[x[0]] * 13 + int(x[1:]) - 2 for x in cardList]

SUITS_TO_VAL = {
	"s": 0,
	"c": 1,
	"d": 2,
	"h": 3

}
class goto(Exception):
	pass

class Worker(QObject):
	def __init__(self,sup):
		self.sup = sup
		super().__init__()



	def StartMainLoop (self):
		self.sup.inLine.returnPressed.disconnect()
		self.sup.inLine.returnPressed.connect(self.sup.inputText)

		while 1:
			try:
				self.sup.folded  =False
				self.sup.label.setText("Enter the number of players")

				cards = [[],[],[],[]]
				while not self.sup.inText.isdigit():
					#print(self.sup.inText+"a  a")
					time.sleep(0.5)

				print(self.sup.inText)

				self.numP = int(self.sup.inText)
				self.sup.inText =''

				self.sup.label.setText("enter your hand")

				self.sup.buttonGo.setEnabled(True)
				self.sup.buttonFold.setEnabled(True)

				check = True
				while check:
					if self.sup.folded :
						print("tap")
						raise goto

					if self.sup.inText!= "":
						try:cards[0] = parse_cards(self.sup.inText)
						except :pass
						time0 = time.perf_counter()
						self.sup.inText = ""

						if len(cards[0]) == 2:
							print(self.numP,cards)
							check = False
							self.data = run_MonteCarlo(cards,opponents=self.numP)
							self.sup.repr_data(self.data)
							print (time.perf_counter()-time0)
					time.sleep(1)
				print('try')


				self.sup.label.setText("Enter the number of players")
				while not self.sup.inText.isdigit():
					time.sleep(0.5)

				self.numP = int(self.sup.inText)
				self.sup.inText =''

				self.sup.label.setText("enter your flop")
				check = True
				while check:
					if self.sup.folded :
						print("tap")
						raise goto

					if self.sup.inText != "":
						try:
							cards[1] = parse_cards(self.sup.inText)
						except:
							pass
						time0 = time.perf_counter()
						self.sup.inText = ""

						if len(cards[1]) == 3:
							print(self.numP)
							check = False
							self.data = run_MonteCarlo(cards, opponents=self.numP)
							self.sup.repr_data(self.data)
							print(self.data)
							print(time.perf_counter() - time0)
					time.sleep(1)
				print('try')


				self.sup.label.setText("Enter the number of players")
				while not self.sup.inText.isdigit():
					time.sleep(0.5)

				self.numP = int(self.sup.inText)
				self.sup.inText = ''

				self.sup.label.setText("enter the turn")
				check = True
				while check:
					if self.sup.folded :
						raise goto

					if self.sup.inText != "":
						try:
							cards[2] = parse_cards(self.sup.inText)
						except:
							pass
						time0 = time.perf_counter()
						self.sup.inText = ""

						if len(cards[2]) == 1:
							print(self.numP)
							check = False
							self.data = run_MonteCarlo(cards, opponents=self.numP)
							self.sup.repr_data(self.data)
							print(self.data)
							print(time.perf_counter() - time0)
					time.sleep(1)


				self.sup.label.setText("Enter the number of players")
				while not self.sup.inText.isdigit():
					time.sleep(0.5)

				self.numP = int(self.sup.inText)
				self.sup.inText = ''

				self.sup.label.setText("enter the river")
				check = True
				while check:
					if self.sup.folded :
						raise goto

					if self.sup.inText != "":
						try:
							cards[3] = parse_cards(self.sup.inText)
						except:
							pass
						time0 = time.perf_counter()
						self.sup.inText = ""

						if len(cards[3]) == 1:

							check = False
							print(self.numP)
							self.data = run_MonteCarlo(cards, opponents=self.numP)
							self.sup.repr_data(self.data)
							print(self.data)
							print(time.perf_counter() - time0)
					time.sleep(1)
				print('try')

			except goto as exp:
				print(exp)
				pass



class win (QMainWindow):
	def __init__(self):
		super().__init__()
		self.active_index = 0
		self.hand = []
		self.flop = []
		self.turn = []
		self.river = []

		self.inText = ""
		self.active_list = [self.hand, self.flop, self.turn, self.river]
		self.simObj = Worker(self)
		self.initUI()

		self.folded = False
		self.thread = QThread()

		self.thread.start()

		self.simObj.moveToThread(self.thread)

		self.thread.started.connect(self.simObj.StartMainLoop)




	def initUI( self ):
		self.setWindowTitle("Poker")
		self.resize(500,100)
		self.widget = QWidget(self)
		self.setCentralWidget(self.widget)

		self.grid = QGridLayout()
		self.widget.setLayout(self.grid)

		self.label = QLabel("Start the game",self)
		self.label.resize(200,30)
		self.grid.addWidget(self.label,0,0,1,2)

		self.labelWins = QLabel("wins :", self)
		self.labelWins.resize(200, 30)
		self.grid.addWidget(self.labelWins, 3, 0, 1, 1)

		self.labelLoss = QLabel("losses :", self)
		self.labelLoss.resize(200, 30)
		self.grid.addWidget(self.labelLoss, 4, 0, 1, 1)

		self.labelTies = QLabel("ties :", self)
		self.labelTies.resize(200, 30)
		self.grid.addWidget(self.labelTies, 5, 0, 1, 1)

		self.labelWinsText = QLabel("", self)
		self.labelWinsText.resize(200, 30)
		self.grid.addWidget(self.labelWinsText, 3, 1, 1, 1)

		self.labelLossText = QLabel("", self)
		self.labelLossText.resize(200, 30)
		self.grid.addWidget(self.labelLossText, 4, 1, 1, 1)

		self.labelTiesText = QLabel("", self)
		self.labelTiesText.resize(200, 30)
		self.grid.addWidget(self.labelTiesText, 5, 1, 1, 1)


		self.inLine= QLineEdit("",self)
		self.inLine.resize(200,40)
		self.grid.addWidget(self.inLine,1,0)
		self.inLine.returnPressed.connect(self.simObj.StartMainLoop)




		self.buttonGo  = QPushButton("Go", self)
		self.buttonGo.resize(200, 100)
		self.buttonGo.setDefault(True)
		self.buttonGo.setEnabled(False)
		self.grid.addWidget(self.buttonGo, 1, 1)
		self.buttonGo.clicked.connect(self.inputText)

		self.buttonFold  = QPushButton("Fold", self)
		self.buttonFold.resize(200, 100)
		self.buttonFold.setEnabled(False)
		self.grid.addWidget(self.buttonFold, 2, 0, 1, 2)
		self.buttonFold.clicked.connect(self.goto1)


		self.widget.setLayout(self.grid)
		self.show()

	def inputText(self):
		self.inText = self.inLine.text()
		self.inLine.clear()

	def repr_data(self,data):
		print(data)
		self.labelWinsText.setText( str(data[0])[:6])
		self.labelLossText.setText(str( data[1])[:6])
		self.labelTiesText.setText( str(data[2])[:6])

	def goto1(self):
		self.folded = True



if __name__ == "__main__":
	app= QApplication(sys.argv)
	ex  = win()

	sys.exit(app.exec_())



