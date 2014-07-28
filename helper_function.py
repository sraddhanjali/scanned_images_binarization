import cv2
import os
import numpy as np


def img_write(img, full_filename, full_directory):
    filename = os.path.basename(full_filename)
    directory = os.path.basename(os.path.dirname(full_filename))
    full_directory += directory
    if not os.path.exists(directory):
        os.makedirs(full_directory)
    full_path = full_directory +"/" + filename
    cv2.imwrite(full_path, img)


def show_wait(img, delay):
    cv2.imshow("image", img)
    cv2.waitKey(delay)


def img_divide(img, size):
    """Divide an image into images blocks of 'size' pixels each
    :rtype : nd array
    """
    for column in range(0, img.shape[0], size):
        height = column+size
        for row in range(0, img.shape[1], size):
            width = row+size
            temp = img[column:height, row:width]
            temp = img_adaptive_otsu(temp)
            img[column:height, row:width] = img_contour_smooth(temp)
    return img

#TODO learning based binarization aka SVM integration
def img_adaptive_otsu(block):
    # print type(block)
    """This is where the adaptive threshold implementation occurs based on local otsu threshold value for each block """
    # standard defined
    set_mean = 90
    set_sd = 20
    mean_block = np.mean(block)
    sd_block = np.std(block)
    if sd_block > set_sd:
        ret, block = cv2.threshold(block, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
    elif sd_block < set_sd:
        if mean_block > set_mean:
            block[:] = 0
        else:
            block[:] = 255
    return block

#TODO smooth and sharpen the binarized content to improve quality
def img_contour_smooth(img):
    img = cv2.GaussianBlur(img, (3, 3), 0.1)
    return img