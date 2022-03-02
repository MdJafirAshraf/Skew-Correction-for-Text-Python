# Import the libraries
import cv2
import argparse
import numpy as np


# Wrap transformation with rectangle co-ordinations
def WrapTransformation(image, points, width, height):

    # Define Input and Output Formation
    inputForm = np.float32(points)
    outputForm = np.float32([[0, 0], [width, 0], [width, height], [0, height]])

    # Calculates a perspective transform from four pairs of the corresponding points
    matrix = cv2.getPerspectiveTransform(inputForm, outputForm)
    # WarpPerspective transforms the source image using the specified matrix
    WrapImage = cv2.warpPerspective(image, matrix, (width, height),
                                    cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT, borderValue=(0, 0, 0))

    return WrapImage


# Skew Correction with input image
def SkewCorrection(image):

    # Get the height and width from image
    (height, width) = image.shape[:2]
    # Copy of image
    image_copy = image.copy()

    # Covert to grayscale
    gray = cv2.cvtColor(image_copy, cv2.COLOR_BGR2GRAY)
    # Blurs an image using a Gaussian filter
    blur = cv2.GaussianBlur(gray, (7, 7), 0)
    # Applies a fixed-level threshold to each array element
    thresh = cv2.threshold(
        blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # Returns a structuring element of the specified size and shape for morphological operations
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    # Dilates an image by using a specific structuring element
    dilate = cv2.dilate(thresh, kernel, iterations=4)

    # Finds contours in a dilate image
    cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]

    # Find a rectangle of the minimum area enclosing the input 2D point set
    rect = cv2.minAreaRect(cnts[0])
    box = np.int0(cv2.boxPoints(rect))
    # Draws contours outlines or filled contours
    cv2.drawContours(image_copy, [box], 0, (36, 255, 12), 3)

    # Adjust box  co-ordinates in correct position
    box = box.tolist()
    if box[0][1] > box[1][0]:
        first_value = box[0]
        box.remove(box[0])
        box.append(first_value)

    # Need to avoid negative co-ordinates
    '''
    coords = []
    for val in box:
        lst = []
        for x in val:
            if x < 0:
                x = 0
            lst.append(x)
        coords.append(lst)
    '''

    # Finally, Wrap Transformation with preprocess image
    # You need to avoid negative co-ordinates, you will use above commented code
    # And change the WrapTransformation function parameter 'box' to 'coords'
    img_wrap = WrapTransformation(image, box, width, height)
    # Resizes an image
    img_out = cv2.resize(img_wrap, (width+70, height))

    # Display the  output image
    cv2.imshow("Rotated_image", img_out)
    # Save the the image in images directory
    cv2.imwrite("images/Rotated_image.jpg", img_out)
    cv2.imshow('Input_image', image)
    cv2.waitKey(0)


if __name__ == '__main__':

    # Construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True,
                    help="path to input image")
    args = vars(ap.parse_args())

    # Loads an image from a file
    image = cv2.imread(args["image"])
    # Pass the image in Skew Correction function
    SkewCorrection(image)
