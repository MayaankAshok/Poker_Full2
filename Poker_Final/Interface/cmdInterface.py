from .MonteCarloReturn import run_MonteCarlo

SUITS_TO_VAL = {
	"s": 0,
	"c": 1,
	"d": 2,
	"h": 3

}


class goto1(Exception):
	pass

def display(l):
	print(f"Wins   : {l[0]}%\n"
	      f"Losses : {l[1]}%\n"
	      f"Ties   : {l[2]}%")

def parse_cards ( cardsIn: str ):
	cardList = cardsIn.split(" ")
	return [SUITS_TO_VAL[x[0]] * 13 + int(x[1:]) - 2 for x in cardList]


def playGame ():
	while True:
		try:
			numPlayers = int(input("How many players?: "))

			check = True
			while check:
				cardsIn = input("Enter your Hand : ")
				if cardsIn != "fold":
					hand = parse_cards(cardsIn)
					#print(hand)
					if len(hand) == 2:
						check = False
						display(run_MonteCarlo([hand,[],[],[]], opponents=numPlayers - 1))
					else:
						print("Enter exactly two cards")
				else:
					raise goto1

			check = True
			while check:
				cardsIn = input("Enter the Flop : ")
				if cardsIn != "fold":
					flop = parse_cards(cardsIn)
					#print(flop)
					if len(flop) == 3:
						check = False
						display(run_MonteCarlo([hand, flop, [], []], opponents=numPlayers - 1))
					else:
						print("Enter exactly three cards")
				else:
					raise goto1

			check = True
			while check:
				cardsIn = input("Enter the turn : ")
				if cardsIn != "fold":
					turn = parse_cards(cardsIn)
					#print(turn)
					if len(turn) == 1:
						display(run_MonteCarlo([hand, flop,turn, []], opponents=numPlayers - 1))
						check = False
					else:
						print("enter exactly one card")
				else:
					raise goto1

			check = True
			while check:
				cardsIn = input("Enter the River : ")
				if cardsIn != "fold":
					river = parse_cards(cardsIn)
					print(river)
					if len(river) == 1:
						display(run_MonteCarlo([hand,flop,turn,river], opponents=numPlayers - 1))
						check = False
					else:
						print("enter exactly one card")
				else:
					raise goto1

		except goto1:
			pass

		#check2 = input("Do you want to Continue ? [y/n] :")
		print("------------------------")
		print("--- NEW HAND ---")
		print("------------------------")




playGame()

'''


	0: 'S2',    1: 'S3',    2: 'S4',    3: 'S5',    4: 'S6',    5: 'S7',
	6: 'S8',    7: 'S9',    8: 'S10',   9: 'S11',   10: 'S12',  11: 'S13',
	12: 'S14',  13: 'C2',   14: 'C3',   15: 'C4',   16: 'C5',   17: 'C6',
	18: 'C7',   19: 'C8',   20: 'C9',   21: 'C10',  22: 'C11',  23: 'C12',
	24: 'C13',  25: 'C14',  26: 'D2',   27: 'D3',   28: 'D4',   29: 'D5',
	30: 'D6',   31: 'D7',   32: 'D8',   33: 'D9',   34: 'D10',  35: 'D11',
	36: 'D12',  37: 'D13',  38: 'D14',  39: 'H2',   40: 'H3',   41: 'H4',
	42: 'H5',   43: 'H6',   44: 'H7',   45: 'H8',   46: 'H9',   47: 'H10',
	48: 'H11',  49: 'H12',  50: 'H13',  51: 'H14'
'''
