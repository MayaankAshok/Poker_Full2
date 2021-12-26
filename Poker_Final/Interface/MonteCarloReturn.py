import time

from .randomRev import Random
from ..Main.Evaluator import runEval

RANKS = ["Straight Flush",
         "Four of a Kind",
         "Full House",
         "Flush",
         "Straight",
         "Three of a Kind",
         "Two Pair",
         "Pair",
         "High Card"]
RANK_SPLIT = {
	range(1, 11): "Straight Flush",
	range(11, 167): "Four of a Kind",
	range(167, 323): "Full House",
	range(323, 1600): "Flush",
	range(1600, 1610): "Straight",
	range(1610, 2468): "Three of a Kind",
	range(2468, 3326): "Two Pair",
	range(3326, 6186): "Pair",
	range(6186, 7463): "High Card"
}


def gen_cards5(opps=1, new_deck=[]):
	req_Cards = 5 + 2 * opps
	cards = sampler(new_deck, req_Cards)
	return cards[:3], [cards[3]], [cards[4]], list(zip(*(iter(cards[5:]),) * 2))


def gen_cards2(opps=1, new_deck=[]):
	req_Cards = 2 + 2 * opps
	cards = sampler(new_deck, req_Cards)
	return [cards[0]], [cards[1]], list(zip(*(iter(cards[2:]),) * 2))


def gen_cards1(opps=1, new_deck=[]):
	req_Cards = 1 + 2 * opps
	cards = sampler(new_deck, req_Cards)
	return [cards[0]], list(zip(*(iter(cards[1:]),) * 2))


def gen_cards0(opps=1, new_deck=[]):
	req_Cards = 2 * opps
	cards = sampler(new_deck, req_Cards)
	return list(zip(*(iter(cards),) * 2))


def run_MonteCarlo(hand: list, opponents=1, reps=2*(10**5)):
	global sampler
	sampler = Random().sample
	time0 = time.perf_counter()
	reps = int(reps / (opponents + 1))

	wins = [0, 0, 0]
	Split = [0, 0, 0, 0, 0, 0, 0, 0, 0]

	hand1 = hand[0]
	flop = hand[1]
	turn = hand[2]
	river = hand[3]

	if len(flop) == 0:  # only hand given
		newDeck = [n for n in range(52) if n not in hand1]
		for _ in range(reps):

			flop, turn, river, handsV = gen_cards5(opponents, newDeck)
			x1 = runEval(hand1 + flop + turn + river)
			xV = [runEval(list(n) + flop + turn + river) for n in handsV]
			#print(xV)
			if x1 < min(xV):
				wins[0] += 1
			elif x1 == min(xV):
				wins[2] += 1
			else:
				wins[1] += 1

	elif len(turn) == 0:  # hand and flop given
		newDeck = [n for n in range(52) if n not in hand1 + flop]
		for _ in range(reps):

			turn, river, handsV = gen_cards2(opponents, newDeck)
			x1 = runEval(hand1 + flop + turn + river)
			xV = [runEval(list(n) + flop + turn + river) for n in handsV]

			if x1 < min(xV):
				wins[0] += 1
			elif x1 == min(xV):
				wins[2] += 1
			else:
				wins[1] += 1

	elif len(river) == 0:  # hand , flop, and turn given
		newDeck = [n for n in range(52) if n not in hand1 + flop + turn]
		for _ in range(reps):

			river, handsV = gen_cards1(opponents, newDeck)
			x1 = runEval(hand1 + flop + turn + river)
			xV = [runEval(list(n) + flop + turn + river) for n in handsV]

			if x1 < min(xV):
				wins[0] += 1
			elif x1 == min(xV):
				wins[2] += 1
			else:
				wins[1] += 1

	else:  # all hand,flop,turn,river given
		newDeck = [n for n in range(52) if n not in hand1 + flop + turn + river]
		for _ in range(reps):
			handsV = gen_cards0(opponents, newDeck)

			x1 = runEval(hand1 + flop + turn + river)
			xV = [runEval(list(n) + flop + turn + river) for n in handsV]

			if x1 < min(xV):
				wins[0] += 1
			elif x1 == min(xV):
				wins[2] += 1
			else:
				wins[1] += 1

	winsP = [round(100 * n / (wins[0] + wins[1] + wins[2]),3) for n in wins]
	# Split = [100*n/np.sum(Split) for n in Split]
	print("Done in : ", time.perf_counter() - time0)

	return winsP


if __name__ == "__main__":

	x = run_MonteCarlo([[10, 5], [], [], []], opponents=19)
	print(x)
'''
	a list of all numbers from 1 to 51 and corresponding cards
	11 = Jack   12 = Queen  13 = King   14 = Ace
	S,C,D,H are Spades,Clubs,Diamonds,Hearts respectively

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
"""
AA = 64.2



"""
