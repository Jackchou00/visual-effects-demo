import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import time


def get_time(f):
    def inner(*arg, **kwarg):
        s_time = time.time()
        res = f(*arg, **kwarg)
        e_time = time.time()
        print("耗时：{}秒".format(e_time - s_time))
        return res

    return inner


""" 
a=np.arange(0,256,1,dtype=float)
b=np.linspace(0,255,256)
print(np.array_equal(a,b)), output: True
"""

bit_depth = 10
a = np.linspace(0, 1, 2**bit_depth)

patch_width = 5
b = np.zeros(2**bit_depth * patch_width)

for i in range(0, patch_width):
    b[i::patch_width] = a

Image_height = 1440
c = np.zeros([1440, 2**bit_depth * patch_width])
for i in range(0, Image_height):
    c[i, ...] = b
