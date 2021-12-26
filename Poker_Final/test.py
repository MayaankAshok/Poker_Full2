import pyautogui as pag
import time
import random
import cProfile
import numpy as np
# %%
BUTTON_FOLD = (1984, 1568)
BUTTON_CHECK = (2236, 1569)
BUTTON_CALL = (2488, 1568)
BUTTON_RAISE = (2399, 1643)
BUTTON_ALLIN = (2391, 1728)
SLIDER_RAISE = ((1819, 1713), (2224, 1715))

FLOP_1 = ((1343, 960), (1432, 1076))
FLOP_2 = ((1453, 960), (1542, 1080))
FLOP_3 = ((1561, 960), (1652, 1078))
HAND_1 = ((1419, 1534), (1548, 1703))
HAND_2 = ((1574, 1535), (1708, 1702))
#%%
time.sleep(2)
pag.click()
print(pag.position())
time.sleep(3)
pag.click()
print(pag.position())
#%%
import PIL.ImageGrab
time.sleep(2)
image = PIL.ImageGrab.grab(bbox=HAND_1[0]+HAND_1[1])
image.show()
#%%
def func():
	x = range(52)
	c  = [random.sample(x,7) for _ in range(int((10**6)/2)) ]
	return c
cProfile.run('func()',sort = 1)
#%%
def func():
	x = range(52)
	c  = [np.random.choice(x,7) for _ in range(int((10**6)/2)) ]
	return c
cProfile.run('func()',sort = 1)