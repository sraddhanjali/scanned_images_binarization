"""
A binarization method with learning-built rules for document images
produced by cameras
Chien-Hsing Chou a, Wen-Hsiung Lin b, Fu Chang b

Features:

Threshold_otsu = TO
Threshold_min = TM
1. TO(r) - TM(r)
2. Mean(r)
3. SD(r)

Actions:

1. LT = 0
2. LT = 255
3. LT = TO(r)
4. LT = TM(r)

"""
import cv2
import helper_function as hf

img = cv2.imread("test/grayscale.png")
img = hf.img_divide(img)
hf.show_wait(img)