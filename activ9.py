""" ==============================================================================================
File: actic9.py
Author: Susan Fox
Date: Fall 2025

Contains functions to practice with Numpy commands, image arithmetic, and more.
==================================================================================================
"""

import cv2
import numpy as np

# -----------------------------------------------------------------------------------------------------------
# blackCanvas

# TODO: Put your definition of blackCanvas here


# -----------------------------------------------------------------------------------------------------------
# rgbStripes

# TODO: Put your definition of rgbStripes here

# -----------------------------------------------------------------------------------------------------------
# phaseBlend 

# TODO: Put your definition of phaseBlend here

# -----------------------------------------------------------------------------------------------------------
# colorShuffle

# TODO: Put your definition of colorShuffle here


# -----------------------------------------------------------------------------------------------------------
# colorShow

# TODO: Put your definition of colorShow here


# -----------------------------------------------------------------------------------------------------------
# jigsawPuzzle

# TODO: Put your definitino of jigsawPuzzle here


# -----------------------------------------------------------------------------------------------------------
# Main script

if __name__ == "__main__":
    # Test calls for blackCanvas
    print("Testing blackCanvas")
    # b1 = blackCanvas(50, 50)
    # cv2.rectangle(b1, (20, 20), (30, 30), (0, 0, 255), -1)
    # cv2.imshow("b1", b1)

    # TODO: Add more calls to blackCanvas here

    # cv2.waitKey()

    # Test calls for rgbStripes
    print("Testing rgbStripes")
    # r1 = rgbStripes(400, 600)
    # cv2.imshow("Stripes 1", r1)

    # TODO: Add more calls to rgbStripes here

    # cv2.waitKey()

    # Subtracting images experiments
    print("Experimenting with arithmetic")

    # TODO: Add script commands to read in two frames and compute the difference in three different ways

    # Blending images
    print("Experimenting with image blending")

    # TODO: Pick three images and read them in here, calling them img1, img2, img3

    # TODO: Resize the 2nd and 3rd image to match img1 here

    # TODO: Put experiments with blending here

    print("Testing phaseBlend")

    # TODO: Put testing calls to phaseBlend here

    # split and merge
    print("Experimenting with split and merge")
    flowerIm = cv2.imread("SampleImages/wildcolumbine.jpg")
    (blueChan, greenChan, redChan) = cv2.split(flowerIm)
    cv2.imshow("Original", flowerIm)
    cv2.imshow("Blue channel alone", blueChan)
    cv2.imshow("Green channel alone", greenChan)
    cv2.imshow("Red channel alone", redChan)
    cv2.waitKey()

    # TODO: Put experiments with split and merge here

    print("Testing colorShuffle")

    # TODO: Put test calls to colorShuffle here

    print("Experiments with Numpy slicing")
    arr1 = np.array([[2, 4, 6, 8], [3, 6, 9, 12], [4, 8, 12, 16]])
    print(arr1)
    print("last of second row:", arr1[1, 3])
    print("second of last row:", arr1[2, 1])
    print("middle values:", arr1[1, 1:3])
    print("third and fourth columns:")
    print(arr1[:, 2:4])
    
    # TODO: Put your experiments with Numpy slicing here