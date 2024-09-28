import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imsave
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


def generate_img(bit_depth=10, Image_width=3072):
    a = np.linspace(0, 2**bit_depth - 1, 2**bit_depth)

    Image_width = 3072
    patch_width = Image_width // (2**bit_depth)
    b = np.zeros(2**bit_depth * patch_width)

    for i in range(0, patch_width):
        b[i::patch_width] = a

    Image_height = 1440
    c = np.zeros([1440, 2**bit_depth * patch_width])
    for i in range(0, Image_height):
        c[i, ...] = b
    c = c.astype(np.uint16)
    c = c * 2 ** (16 - bit_depth)

    image = Image.fromarray(c, mode="I;16")
    return image


image_8 = generate_img(8)
image_10 = generate_img(10)

image_8.save("8bit.tiff")
image_10.save("10bit.tiff")
