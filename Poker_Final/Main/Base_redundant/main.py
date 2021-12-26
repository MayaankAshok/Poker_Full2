import time

import numpy as np

from Lookup import LU_FLUSH, LU_OTHER

RANK_VALUES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
SUIT_VALUES = [2, 3, 5, 7]
FLUSH_CHECK = {128, 11907, 168070, 2187, 31250, 46875, 67228, 288, 672, 800, 1568, 235298, 153125, 78125, 1458, 352947,
               8505, 6075, 3645, 18750, 109375, 320, 448, 192, 252105, 3402, 972, 420175, 12500, 588245, 65625, 28125,
               151263, 480, 1120, 43750, 100842, 5103, 823543, 2430}
print(len(FLUSH_CHECK))

def store_cards(cardlist):
	return [(SUIT_VALUES[n // 13] << 8) + RANK_VALUES[n % 13] for n in cardlist]


def setValue(c):
	if ((c[0] & 0x700) >> 8) * ((c[1] & 0x700) >> 8) * ((c[2] & 0x700) >> 8) * ((c[3] & 0x700) >> 8) * (
			(c[4] & 0x700) >> 8) * ((c[5] & 0x700) >> 8) * ((c[6] & 0x700) >> 8) in FLUSH_CHECK:
		equi = LU_FLUSH[np.prod(
			[x & 0x3F for x in c if
			 (x & 0x700) >> 8 == max([(x & 0x700) >> 8 for x in c], key=[(x & 0x700) >> 8 for x in c].count)]
			, dtype=np.int64)]

	else:
		equi = LU_OTHER[np.prod(
			[int(x & 0x3F) for x in c], dtype=np.int64)]

	return equi


def eval_hand(cards=[]):
	return setValue([(SUIT_VALUES[n // 13] << 8) + RANK_VALUES[n % 13] for n in cards])


val_to_prime = {
	'2': 2,
	'3': 3,
	'4': 5,
	'5': 7,
	'6': 11,
	'7': 13,
	'8': 17,
	'9': 19,
	'T': 23,
	'J': 29,
	'Q': 31,
	'K': 37,
	'A': 41

}


def eval_flush(c=[]):
	return LU_FLUSH[np.prod([val_to_prime[r] for r in c], dtype=np.int64)]


def eval_other(c=[]):
	return LU_OTHER[np.prod([val_to_prime[r] for r in c], dtype=np.int64)]


# %%
if __name__ == "__main__":
	t = 0
	time0 = time.perf_counter()
	x = store_cards([38, 51, 25, 13, 14, 15, 17])
	for n in range(10**5):
		a = setValue(x)

	t += 1

	print(time.perf_counter() - time0)
	print(x)

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
