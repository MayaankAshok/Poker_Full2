import random
import time
import os


import numpy as np
script_dir = os.path.dirname(__file__)
s4 = np.load(os.path.join(script_dir, r'./Archive/arch4.npy'))
s5 = np.load(os.path.join(script_dir, r'./Archive/arch5.npy'))
s6 = np.load(os.path.join(script_dir, r'./Archive/arch6.npy'))
s7 = np.load(os.path.join(script_dir, r'./Archive/arch7.npy'))


def runEval(cards=[]):
	return s7[s6[s5[s4[cards[0]][cards[1]][cards[2]][cards[3]]][cards[4]]][cards[5]]][cards[6]]



# if __name__ == '__main__':
# 	time0 = time.perf_counter()
# 	c = random.sample(range(52), 7)
# 	for _ in range(10**5):
# 		x = runEval(c)
# 	print(c, time.perf_counter() - time0)
