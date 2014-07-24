import cv2
import numpy as np
import matplotlib
from math import sqrt, log, exp


def img_write(img):
    cv2.imwrite("rtscloseresult.jpg", img)


def show_wait(img):
    cv2.imshow("image", img)
    cv2.waitKey(0)


def img_divide(img, size=3):
    """Divide an image into images blocks of size 100 pixels each
    :rtype : list
    """
    for column in range(0, img.shape[1], size):
        for row in range(0, img.shape[0], size):
            if column + size <= img.shape[1]:
                if row + size <= img.shape[0]:
                    new = img[column:column+size, row:row+size]
                    new = img_adaptive_otsu(new)
                    img[column:column+size, row:row+size] = new
            else:
                return img


def img_adaptive_otsu(block):
    """This is where the adaptive threshold implementation occurs based on local otsu value for each block image"""
    set_mean = 128
    set_sd = 15

    mean = np.mean(block)
    sd = np.std(block)

    if sd > set_sd:
        ret, block = cv2.threshold(block, 0, 255, cv2.THRESH_OTSU)
    elif mean > set_mean:
        block[:] = 255
    elif mean <= meanthreshold:
        block[:] = 0
    return block

