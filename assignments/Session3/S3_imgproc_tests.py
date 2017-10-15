## @namespace S3_imgproc_tests
# A set of tests for the generic functions for image management
#
# @author Benoit Lamit, LPro DIM, IUT Annecy le vieux, FRANCE

import imp;
import pytest;
import cv2;

imgproc_tools = imp.load_source('S3_imgproc_tools', 'assignments/Session3/S3_imgproc_tools.py');

@pytest.fixture
def empty_fixture():
    return None;

@pytest.fixture
def grayscale_image():
    return cv2.imread('assignments/Session3/myimage.jpg',0);

@pytest.fixture
def color_image():
    return cv2.imread('assignments/Session3/myimage.jpg',1);

""" INVERT_COLOR_MANUAL"""


## Tests the invert_color_manual function, using an empty fixture
#
# @param empty_fixture : the empty fixture for the test
def test_invert_colors_manual_with_empty_fixture(empty_fixture):
    with pytest.raises(ValueError) as verrinfo:
        imgproc_tools.invert_colors_manual(empty_fixture);
    assert 'Please provide a valid image' in str(verrinfo.value);

## Tests the invert_color_manual function, using a grayscale image
#
# @param grayscale_image : the grayscale image for the test
def test_invert_colors_manual_with_grayscale_image(grayscale_image):
    inverted_image = imgproc_tools.invert_colors_manual(grayscale_image);

    inverted = True;

    for x in xrange(inverted_image.shape[0]-1):
        for y in xrange(inverted_image.shape[0]-1):
            inverted = (grayscale_image[x][y] + inverted_image[x][y] == 255);
            if not inverted: break;
        if not inverted: break;

    assert inverted;

## Tests the invert_color_manual function, using a color image
#
# @param color_image : the color image for the test
def test_invert_colors_manual_with_color_image(color_image):
    inverted_image = imgproc_tools.invert_colors_manual(color_image);

    inverted = True;

    for x in xrange(inverted_image.shape[0] - 1):
        for y in xrange(inverted_image.shape[0] - 1):
            inverted = (color_image[x][y][0] + inverted_image[x][y][0] == 255);
            if not inverted: break;
            inverted = (color_image[x][y][1] + inverted_image[x][y][1] == 255);
            if not inverted: break;
            inverted = (color_image[x][y][2] + inverted_image[x][y][2] == 255);
            if not inverted: break;
        if not inverted: break;

    assert inverted;


""" THRESHOLD_IMAGE_NUMPY """


## Tests threshold_image_numpy function, using an empty fixture
#
# @param empty_fixture : the empty fixture for the test
def test_threshold_image_numpy_with_empty_fixture(empty_fixture):
    with pytest.raises(ValueError) as verrinfo:
        imgproc_tools.threshold_image_numpy(empty_fixture, 127);
    assert 'Please provide a valid image' in str(verrinfo.value);

## Tests threshold_image_numpy function, using a grayscale image
#
# @param grayscale_image : the grayscale image for the test
def test_threshold_image_numpy_with_grayscale_image(grayscale_image):
    threshold = 127;
    compressed_image = imgproc_tools.threshold_image_numpy(grayscale_image, threshold);

    compressed = True;

    for x in xrange(compressed_image.shape[0] - 1):
        for y in xrange(compressed_image.shape[0] - 1):
            compressed = \
                (grayscale_image[x][y] >= threshold == compressed_image[x][y]) \
                or \
                (threshold >= grayscale_image[x][y] == compressed_image[x][y]);
            if not compressed: break;
        if not compressed: break;

    assert compressed;

## Tests the threshold_image_numpy function, using a color image
#
# @param color_image : the color image for the test
def test_threshold_image_numpy_with_color_image(color_image):
    threshold = [100, 125, 150];
    compressed_image = imgproc_tools.threshold_image_numpy(color_image, threshold);

    compressed = True;

    for x in xrange(compressed_image.shape[0] - 1):
        for y in xrange(compressed_image.shape[0] - 1):
            compressed = \
                (color_image[x][y][0] >= threshold[0] == compressed_image[x][y][0]) \
                or \
                (threshold[0] >= color_image[x][y][0] == compressed_image[x][y][0]);
            if not compressed: break;
            compressed = \
                (color_image[x][y][1] >= threshold[1] == compressed_image[x][y][1]) \
                or \
                (threshold[1] >= color_image[x][y][1] == compressed_image[x][y][1]);
            if not compressed: break;
            compressed = \
                (color_image[x][y][2] >= threshold[2] == compressed_image[x][y][2]) \
                or \
                (threshold[2] >= color_image[x][y][2] == compressed_image[x][y][2]);
            if not compressed: break;
        if not compressed: break;

    assert compressed;