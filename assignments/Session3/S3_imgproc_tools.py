## @namespace S3_imgproc_tools
# A set of generic functions for image management
#
# @author Benoit Lamit, LPro DIM, IUT Annecy le vieux, FRANCE

import cv2;
import numpy;

"""
img_gray=cv2.imread('myimage.jpg',0);
img_bgr=cv2.imread('myimage.jpg',1);

print("Gray levels image shape = "+str(img_gray.shape));
print("BGR image shape = "+str(img_bgr.shape));

#display the loaded images
cv2.imshow("Gray levels image", img_gray);
cv2.imshow("BGR image", img_bgr);
cv2.waitKey();
"""

## Invert the value of each pixel on each color canal
#
# @param input_img : an numpy array holding the input image data
# @return the color inverted image as numpy array
def invert_colors_manual(input_img):

    # Check if empty
    if type(input_img) is not numpy.ndarray or input_img.shape == (0, 0):
        raise ValueError('Please provide a valid image');

    # If not, create the new image
    color_scale = 'RGB' if input_img.ndim == 3 else 'GrayScale'; # pythonic ternary

    if color_scale == 'RGB' :
        output_img = numpy.zeros((input_img.shape[0], input_img.shape[1], 3), input_img.dtype);
    else:
        output_img = numpy.zeros((input_img.shape[0], input_img.shape[1]), input_img.dtype);

    # Then iterate through input data to compute output
    if color_scale == 'RGB':
        for x in xrange(input_img.shape[0]-1):
            for y in xrange(input_img.shape[1]-1):

                output_img[x][y][0] = 255 - input_img[x][y][0];
                output_img[x][y][1] = 255 - input_img[x][y][1];
                output_img[x][y][2] = 255 - input_img[x][y][2];
    else:
        for x in xrange(input_img.shape[0]-1):
            for y in xrange(input_img.shape[1]-1):

                output_img[x][y] = 255 - input_img[x][y];

    return output_img;