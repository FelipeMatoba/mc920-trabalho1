import sys
import cv2
import matplotlib as plt
import numpy as np
import os.path

def main():
    args = sys.argv[1:]

    if len(args) == 0:
        sys.exit('No image selected!')

    directory = os.path.dirname(os.path.realpath(__file__))
    img_dir = os.path.join(directory, os.pardir, args[0])
    print(img_dir)

    img = cv2.imread(img_dir)

    if img is None:
        sys.exit("Could not read the image.")

    if len(args) == 2:
        o_name = args[1] + '.png'
    else:
        o_name = args[0][:-5] + '1.png'

def apply_mask(mask, img):
    return

if __name__ == "__main__":
    main()