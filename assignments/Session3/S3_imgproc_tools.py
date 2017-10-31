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
# @param input_img : a numpy array holding the input image data
# @return the color inverted image as numpy array
def invert_colors_manual(input_img):

    # Check if empty
    if type(input_img) is not numpy.ndarray or input_img.shape == (0, 0):
        raise ValueError('Please provide a valid image');

    # If not, create the new image
    color_scale = 'RGB' if input_img.ndim == 3 else 'GrayScale'; # pythonic ternary

    if color_scale == 'RGB':
        output_img = numpy.zeros((input_img.shape[0], input_img.shape[1], 3), input_img.dtype);
    else:
        output_img = numpy.zeros((input_img.shape[0], input_img.shape[1]), input_img.dtype);

    # Then iterate through input data to compute output
    if color_scale == 'RGB':
        for x in xrange(input_img.shape[0]-1):
            for y in xrange(input_img.shape[1]-1):
                # Could be a third-level - almost useless - nested loop ...
                output_img[x][y][0] = 255 - input_img[x][y][0];
                output_img[x][y][1] = 255 - input_img[x][y][1];
                output_img[x][y][2] = 255 - input_img[x][y][2];
    else:
        for x in xrange(input_img.shape[0]-1):
            for y in xrange(input_img.shape[1]-1):

                output_img[x][y] = 255 - input_img[x][y];

    return output_img;


## Apply a threshold for the value of each pixel on each color channel
#
# @param input_img : a numpy array holding the input image data
# @return the compressed image as numpy array
def threshold_image_manual(input_img, threshold):

    # Check if empty
    if type(input_img) is not numpy.ndarray or input_img.shape == (0, 0):
        raise ValueError('Please provide a valid image');

    # If not, check the threshold type and its convenience
    color_scale = 'RGB' if input_img.ndim == 3 else 'GrayScale';  # pythonic ternary

    if type(threshold) is int:
        threshold_type = 'Monovalue';
    elif type(threshold) is list and len(threshold) == 3:
        threshold_type = 'Array';
    else:
        raise ValueError('Please provide a convenient threshold value');

    if threshold_type == 'Array' and color_scale is not 'RGB':
        raise ValueError('Please provide a convenient threshold value');

    # If everything is OK, apply the threshold
    if color_scale == 'RGB':
        output_img = numpy.zeros((input_img.shape[0], input_img.shape[1], 3), input_img.dtype);
    else:
        output_img = numpy.zeros((input_img.shape[0], input_img.shape[1]), input_img.dtype);

    if color_scale == 'RGB':
        for x in xrange(input_img.shape[0] - 1):
            for y in xrange(input_img.shape[1] - 1):
                if threshold_type == 'Array':
                    # Could be a third-level - almost useless - nested loop ...
                    output_img[x][y][0] = 255 if input_img[x][y][0] >= threshold[0] else 0;
                    output_img[x][y][1] = 255 if input_img[x][y][1] >= threshold[1] else 0;
                    output_img[x][y][2] = 255 if input_img[x][y][2] >= threshold[2] else 0;
                else:
                    # Could be a third-level - almost useless - nested loop ...
                    output_img[x][y][0] = 255 if input_img[x][y][0] >= threshold else 0;
                    output_img[x][y][1] = 255 if input_img[x][y][1] >= threshold else 0;
                    output_img[x][y][2] = 255 if input_img[x][y][2] >= threshold else 0;
    else:
        for x in xrange(input_img.shape[0] - 1):
            for y in xrange(input_img.shape[1] - 1):
                output_img[x][y] = 255 if input_img[x][y] >= threshold else 0;

    return output_img;


## Apply a threshold for the value of each pixel on each color channel. Uses the numpy library.
#
# @param input_img : a numpy array holding the input image data
# @return the compressed image as numpy array
def threshold_image_numpy(input_img, threshold):

    # Check if empty
    if type(input_img) is not numpy.ndarray or input_img.shape == (0, 0):
        raise ValueError('Please provide a valid image');

    # If not, check the threshold type and its convenience
    color_scale = 'RGB' if input_img.ndim == 3 else 'GrayScale';  # pythonic ternary

    if type(threshold) is int:
        threshold_type = 'Monovalue';
    elif type(threshold) is list and len(threshold) == 3:
        threshold_type = 'Array';
    else:
        raise ValueError('Please provide a convenient threshold value');

    if threshold_type == 'Array' and color_scale is not 'RGB':
        raise ValueError('Please provide a convenient threshold value');

    # If everything is OK, apply the threshold... with kind of magic :o
    output_img = ((input_img > threshold) * 255).astype(input_img.dtype);

    return output_img;


## Apply a threshold for the value of each pixel on each color channel. Uses the opencv OTSU method.
# If no threshold is provided (or if it's null), the optimal one will be chosen and printed
#
# @param input_img : a numpy array holding the input image data
# @return the compressed image as numpy array
def threshold_colors_opencv(input_img):
    # Check if empty
    if type(input_img) is not numpy.ndarray or input_img.shape == (0, 0):
        raise ValueError('Please provide a valid image');

    # If not, check the image type
    color_scale = 'RGB' if input_img.ndim == 3 else 'GrayScale';  # pythonic ternary

    # If everything is OK, apply the threshold
    if color_scale == 'RGB':
        b, g, r = cv2.split(input_img);

        thr_b, out_b = cv2.threshold(b, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU);
        thr_g, out_g = cv2.threshold(g, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU);
        thr_r, out_r = cv2.threshold(r, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU);

        thr = [thr_b, thr_g, thr_r];

        output_img = cv2.merge([out_b, out_g, out_r]);

    else:
        thr, output_img = cv2.threshold(input_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU);

    return thr, output_img;