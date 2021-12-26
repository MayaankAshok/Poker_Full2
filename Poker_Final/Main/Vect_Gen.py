# %% setup
import sys
import time
from collections import Counter
import iteration_utilities
import numpy as np
import Poker_Final.Main.Base_redundant.main as main

np.set_printoptions(threshold=sys.maxsize)

Drank = {
	0: "2",
	1: "3",
	2: "4",
	3: "5",
	4: "6",
	5: "7",
	6: "8",
	7: "9",
	8: "T",
	9: "J",
	10: "Q",
	11: "K",
	12: "A"
}
Dsuit = {
	0: "s",
	1: "c",
	2: "d",
	3: "h"

}
card_to_num = {
	'2s': 0,
	'3s': 1,
	'4s': 2,
	'5s': 3,
	'6s': 4,
	'7s': 5,
	'8s': 6,
	'9s': 7,
	'Ts': 8,
	'Js': 9,
	'Qs': 10,
	'Ks': 11,
	'As': 12,
	'2c': 13,
	'3c': 14,
	'4c': 15,
	'5c': 16,
	'6c': 17,
	'7c': 18,
	'8c': 19,
	'9c': 20,
	'Tc': 21,
	'Jc': 22,
	'Qc': 23,
	'Kc': 24,
	'Ac': 25,
	'2d': 26,
	'3d': 27,
	'4d': 28,
	'5d': 29,
	'6d': 30,
	'7d': 31,
	'8d': 32,
	'9d': 33,
	'Td': 34,
	'Jd': 35,
	'Qd': 36,
	'Kd': 37,
	'Ad': 38,
	'2h': 39,
	'3h': 40,
	'4h': 41,
	'5h': 42,
	'6h': 43,
	'7h': 44,
	'8h': 45,
	'9h': 46,
	'Th': 47,
	'Jh': 48,
	'Qh': 49,
	'Kh': 50,
	'Ah': 51
}
rank_to_num = {
	"2": 0,
	"3": 1,
	"4": 2,
	"5": 3,
	"6": 4,
	"7": 5,
	"8": 6,
	"9": 7,
	"T": 8,
	"J": 9,
	"Q": 10,
	"K": 11,
	"A": 12,
}

convert1 = lambda a: Drank[a % 13] + Dsuit[a // 13]


def checkValidity_7(n1: int, n2: int):
	cardStr: str = dict6_cards[n1]
	cards_num_flush: list = [card_to_num[a + b] for a, b in zip(cardStr[0::2], cardStr[1::2]) if b != 'x']
	cards_num_flush.append(n2)

	cards_num_count = Counter(list(cardStr[::2]) + [Drank[n2 % 13]])
	if len(cards_num_flush) == len(set(cards_num_flush)) and cards_num_count.most_common(1)[0][1] <= 4:
		cards_num_count.most_common(1)[0][1]
		return True
	else:
		return False


def convert7(c6=0, c7=0):
	cardL: str = dict6_cards[c6]
	cards_num: list(int) = [card_to_num[a + b] for a, b in zip(cardL[0::2], cardL[1::2]) if b != 'x']
	cards_x: list(str) = [a + b for a, b in zip(cardL[0::2], cardL[1::2]) if b == 'x']
	cards_num.append(c7)

	counter: Counter = Counter([n // 13 for n in cards_num]).most_common()

	if counter[0][1] < 5:
		return "".join(
			sorted([Drank[card_num % 13] + 'x' for card_num in sorted(cards_num, key=lambda a: a % 13)] + cards_x,
			       key=lambda a: rank_to_num[a[0]]))
	else:
		req_suit = [c[0] for c in counter if c[1] > 2]
		return "".join(
			[Drank[card_num % 13] + Dsuit[card_num // 13] for card_num in sorted(cards_num, key=lambda n: (n % 13, n))
			 if
			 card_num // 13 in req_suit]
			+ sorted(
				[Drank[card_num % 13] + 'x' for card_num in sorted(cards_num, key=lambda n: (n % 13)) if
				 card_num // 13 not in req_suit]
				+ cards_x, key=lambda a: rank_to_num[a[0]]))


def convert6(c5=0, c6=0):
	cardStr: str = dict5_cards[c5]
	cards_num: list(int) = [card_to_num[a + b] for a, b in zip(cardStr[0::2], cardStr[1::2]) if b != 'x']

	cards_num.append(c6)
	if len(cards_num) != len(set(cards_num)):
		return ""

	cards_x: list(str) = [a + b for a, b in zip(cardStr[0::2], cardStr[1::2]) if b == 'x']
	counter_Suit: Counter = Counter([n // 13 for n in cards_num]).most_common()
	counter_Rank: Counter

	if counter_Suit[0][1] < 4:
		return "".join(
			sorted([Drank[card_num % 13] + 'x' for card_num in sorted(cards_num, key=lambda a: a % 13)] + cards_x,
			       key=lambda a: rank_to_num[a[0]]))
	else:
		req_suit = [c[0] for c in counter_Suit if c[1] > 2]
		return "".join(
			[Drank[card_num % 13] + Dsuit[card_num // 13] for card_num in sorted(cards_num, key=lambda n: (n % 13, n))
			 if
			 card_num // 13 in req_suit]
			+ sorted(
				[Drank[card_num % 13] + 'x' for card_num in sorted(cards_num, key=lambda n: (n % 13)) if
				 card_num // 13 not in req_suit]
				+ cards_x, key=lambda a: rank_to_num[a[0]]))


def convert5(c4=0, c5=0):
	cardL: str = dict4_cards[c4]
	cards_num: list(int) = [card_to_num[a + b] for a, b in zip(cardL[0::2], cardL[1::2]) if b != 'x']
	cards_num.append(c5)

	counter: Counter = Counter([n // 13 for n in cards_num]).most_common()
	if len(cards_num) != len(set(cards_num)):
		return ""

	cards_x: list(str) = [a + b for a, b in zip(cardL[0::2], cardL[1::2]) if b == 'x']

	if counter[0][1] < 3:
		return "".join(
			sorted([Drank[card_num % 13] + 'x' for card_num in sorted(cards_num, key=lambda a: a % 13)] + cards_x,
			       key=lambda a: rank_to_num[a[0]]))
	else:
		req_suit = [c[0] for c in counter if c[1] > 2]
		return "".join(
			[Drank[card_num % 13] + Dsuit[card_num // 13] for card_num in sorted(cards_num, key=lambda n: (n % 13, n))
			 if
			 card_num // 13 in req_suit]
			+ sorted(
				[Drank[card_num % 13] + 'x' for card_num in sorted(cards_num, key=lambda n: (n % 13)) if
				 card_num // 13 not in req_suit]
				+ cards_x, key=lambda a: rank_to_num[a[0]]))


def convert4(card_nums=[]):
	counter: Counter = Counter([card_num // 13 for card_num in card_nums]).most_common()
	if counter[0][1] == 1:
		return "".join([Drank[num % 13] + 'x' for num in sorted(card_nums, key=lambda n: (n % 13))])
	else:
		req_suit = [t[0] for t in counter if t[1] >= 2]
		return ("".join(
			[Drank[card_num % 13] + Dsuit[card_num // 13] for card_num in sorted(card_nums, key=lambda n: (n % 13, n))
			 if card_num // 13 in
			 req_suit] + [Drank[card_num % 13] + 'x' for card_num in sorted(card_nums, key=lambda n: (n % 13)) if
			              card_num // 13 not in req_suit]))


# %% initialize 4-card table
state4 = np.empty((52, 52, 52, 52), dtype='<U8')

time0 = time.perf_counter()
for n1 in range(52):
	for n2 in range(52):
		for n3 in range(52):
			for n4 in range(52):
				if len([n1, n2, n3, n4]) == len(set([n1, n2, n3, n4])):
					state4[n1][n2][n3][n4] = convert4([n1, n2, n3, n4])

	print(n1, time.perf_counter() - time0)

list4_cards = list(iteration_utilities.deepflatten(state4.tolist(), types=list))
list4_cards = list(set(list4_cards))

dict4_cards = dict(enumerate(list4_cards))
dict4_rev_cards = dict(zip(dict4_cards.values(), dict4_cards.keys()))

state4_num = np.empty((52, 52, 52, 52), dtype=int)
for n1 in range(52):
	# print(convert(n1))
	for n2 in range(52):
		for n3 in range(52):
			for n4 in range(52):
				if len([n1, n2, n3, n4]) == len(set([n1, n2, n3, n4])):
					state4_num[n1][n2][n3][n4] = dict4_rev_cards[convert4([n1, n2, n3, n4])]
	print(n1, time.perf_counter() - time0)

# %% initialize 5-card table

LEN_4 = 84449

state5 = np.empty((LEN_4, 52), dtype="<U10")
time0 = time.perf_counter()
for n2 in range(52):
	for n1 in range(LEN_4):
		state5[n1][n2] = convert5(n1, n2)
	print(n2, time.perf_counter() - time0)

list5_cards = list(iteration_utilities.deepflatten(state5[1:].tolist(), types=list))
list5_cards = list(set(list5_cards))

dict5_cards = dict(enumerate(list5_cards))
dict5_rev_cards = dict(zip(dict5_cards.values(), dict5_cards.keys()))

time0 = time.perf_counter()
state5_num = np.empty((LEN_4, 52), dtype=int)
for n2 in range(52):
	# print(convert(n1))
	for n1 in range(1, LEN_4):
		state5_num[n1][n2] = dict5_rev_cards[convert5(n1, n2)]
	print(n2, time.perf_counter() - time0)

# %% initialize 6-card table

LEN_5 = 152621

state6 = np.empty((LEN_5, 52), dtype="<U12")
time0 = time.perf_counter()
for n2 in range(52):
	for n1 in range(LEN_5):
		state6[n1][n2] = convert6(n1, n2)
	print(n2, time.perf_counter() - time0)

list6_cards = list(iteration_utilities.deepflatten(state6[1:].tolist(), types=list))
list6_cards = list(set(list6_cards))

dict6_cards = dict(enumerate(list6_cards))
dict6_rev_cards = dict(zip(dict6_cards.values(), dict6_cards.keys()))

time0 = time.perf_counter()
state6_num = np.empty((LEN_5, 52), dtype=int)
for n2 in range(52):
	# print(convert(n1))
	for n1 in range(1, LEN_5):
		state6_num[n1][n2] = dict6_rev_cards[convert6(n1, n2)]
	print(n2, time.perf_counter() - time0)

# %% initialize 7-card table
LEN_6 = 352_613

state7_num = np.empty((LEN_6, 52), dtype=int)
time0 = time.perf_counter()
for n2 in range(52):
	for n1 in range(1, LEN_6):
		if checkValidity_7(n1, n2):
			cards = convert7(n1, n2)
			if cards[1] == 'x':
				state7_num[n1][n2] = main.eval_other(list(cards)[::2])
			else:
				cards = [cards[n] for n in range(0, len(cards), 2) if cards[n + 1] != 'x']
				state7_num[n1][n2] = main.eval_flush(cards)
		else:
			state7_num[n1][n2] = 0
	print(n2, time.perf_counter() - time0)

# %% save the final tables as archive
np.save('Archive/arch7.npy', state7_num)
np.save('Archive/arch6.npy', state6_num)
np.save('Archive/arch5.npy', state5_num)
np.save('Archive/arch4.npy', state4_num)
