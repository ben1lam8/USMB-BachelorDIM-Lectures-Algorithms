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


""" THRESHOLD_IMAGE_MANUAL """


## Tests threshold_image_manual function, using an empty fixture
#
# @param empty_fixture : the empty fixture for the test
def test_threshold_image_manual_with_empty_fixture(empty_fixture):
    with pytest.raises(ValueError) as verrinfo:
        imgproc_tools.threshold_image_manual(empty_fixture, 127);
    assert 'Please provide a valid image' in str(verrinfo.value);

## Tests threshold_image_manual function, using a grayscale image
#
# @param grayscale_image : the grayscale image for the test
def test_threshold_image_manual_with_grayscale_image(grayscale_image):
    threshold = 127;
    thresholded_image = imgproc_tools.threshold_image_manual(grayscale_image, threshold);

    thresholded = True;

    for x in xrange(thresholded_image.shape[0] - 1):
        for y in xrange(thresholded_image.shape[0] - 1):
            thresholded = \
                (grayscale_image[x][y] >= threshold and thresholded_image[x][y] == 255) \
                or \
                (threshold >= grayscale_image[x][y] and thresholded_image[x][y] == 0);
            if not thresholded: break;
        if not thresholded: break;

    assert thresholded;

## Tests the threshold_image_manual function, using a color image
#
# @param color_image : the color image for the test
def test_threshold_image_manual_with_color_image(color_image):
    threshold = [100, 125, 150];
    thresholded_image = imgproc_tools.threshold_image_manual(color_image, threshold);

    thresholded = True;

    for x in xrange(thresholded_image.shape[0] - 1):
        for y in xrange(thresholded_image.shape[0] - 1):
            thresholded = \
                (color_image[x][y][0] >= threshold[0] and thresholded_image[x][y][0] == 255) \
                or \
                (threshold[0] >= color_image[x][y][0] and thresholded_image[x][y][0] == 0);
            if not thresholded: break;
            thresholded = \
                (color_image[x][y][1] >= threshold[1] and thresholded_image[x][y][1] == 255) \
                or \
                (threshold[1] >= color_image[x][y][1] and thresholded_image[x][y][1] == 0);
            if not thresholded: break;
            thresholded = \
                (color_image[x][y][2] >= threshold[2] and thresholded_image[x][y][2] == 255) \
                or \
                (threshold[2] >= color_image[x][y][2] and thresholded_image[x][y][2] == 0);
            if not thresholded: break;
        if not thresholded: break;

    assert thresholded;

## Tests the threshold_image_manual function, using a color image
#
# @param color_image : the color image for the test
def test_threshold_image_manual_with_color_image_and_monovalue_threshold(color_image):
    threshold = 127;
    thresholded_image = imgproc_tools.threshold_image_manual(color_image, threshold);

    thresholded = True;

    for x in xrange(thresholded_image.shape[0] - 1):
        for y in xrange(thresholded_image.shape[0] - 1):
            thresholded = \
                (color_image[x][y][0] >= threshold and thresholded_image[x][y][0] == 255) \
                or \
                (threshold >= color_image[x][y][0] and thresholded_image[x][y][0] == 0);
            if not thresholded: break;
            thresholded = \
                (color_image[x][y][1] >= threshold and thresholded_image[x][y][1] == 255) \
                or \
                (threshold >= color_image[x][y][1] and thresholded_image[x][y][1] == 0);
            if not thresholded: break;
            thresholded = \
                (color_image[x][y][2] >= threshold and thresholded_image[x][y][2] == 255) \
                or \
                (threshold >= color_image[x][y][2] and thresholded_image[x][y][2] == 0);
            if not thresholded: break;
        if not thresholded: break;

    assert thresholded;

## Tests the threshold_image_manual function, using a color image and a unconvenient threshold
#
# @param color_image : the color image for the test
def test_threshold_image_manual_with_unconvenient_threshold(color_image):
    threshold = [100, 125, 150, 123, 145];

    with pytest.raises(ValueError) as verrinfo:
        imgproc_tools.threshold_image_manual(color_image, threshold);
    assert 'Please provide a convenient threshold value' in str(verrinfo.value);

## Tests the threshold_image_manual function, using a color image and a unconvenient threshold type
#
# @param grayscale_image : the grayscale image for the test
def test_threshold_image_manual_with_unconvenient_threshold_type(grayscale_image):
    threshold = [100, 125, 150];

    with pytest.raises(ValueError) as verrinfo:
        imgproc_tools.threshold_image_manual(grayscale_image, threshold);
    assert 'Please provide a convenient threshold value' in str(verrinfo.value);


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
    thresholded_image = imgproc_tools.threshold_image_numpy(grayscale_image, threshold);

    thresholded = True;

    for x in xrange(thresholded_image.shape[0] - 1):
        for y in xrange(thresholded_image.shape[0] - 1):
            thresholded = \
                (grayscale_image[x][y] >= threshold and thresholded_image[x][y] == 255) \
                or \
                (threshold >= grayscale_image[x][y] and thresholded_image[x][y] == 0);
            if not thresholded: break;
        if not thresholded: break;

    assert thresholded;

## Tests the threshold_image_numpy function, using a color image
#
# @param color_image : the color image for the test
def test_threshold_image_numpy_with_color_image(color_image):
    threshold = [100, 125, 150];
    thresholded_image = imgproc_tools.threshold_image_numpy(color_image, threshold);

    thresholded = True;

    for x in xrange(thresholded_image.shape[0] - 1):
        for y in xrange(thresholded_image.shape[0] - 1):
            thresholded = \
                (color_image[x][y][0] >= threshold[0] and thresholded_image[x][y][0] == 255) \
                or \
                (threshold[0] >= color_image[x][y][0] and thresholded_image[x][y][0] == 0);
            if not thresholded: break;
            thresholded = \
                (color_image[x][y][1] >= threshold[1] and thresholded_image[x][y][1] == 255) \
                or \
                (threshold[1] >= color_image[x][y][1] and thresholded_image[x][y][1] == 0);
            if not thresholded: break;
            thresholded = \
                (color_image[x][y][2] >= threshold[2] and thresholded_image[x][y][2] == 255) \
                or \
                (threshold[2] >= color_image[x][y][2] and thresholded_image[x][y][2] == 0);
            if not thresholded: break;
        if not thresholded: break;

    assert thresholded;

## Tests the threshold_image_manual function, using a color image
#
# @param color_image : the color image for the test
def test_threshold_image_numpy_with_color_image_and_monovalue_threshold(color_image):
    threshold = 127;
    thresholded_image = imgproc_tools.threshold_image_numpy(color_image, threshold);

    thresholded = True;

    for x in xrange(thresholded_image.shape[0] - 1):
        for y in xrange(thresholded_image.shape[0] - 1):
            thresholded = \
                (color_image[x][y][0] >= threshold and thresholded_image[x][y][0] == 255) \
                or \
                (threshold >= color_image[x][y][0] and thresholded_image[x][y][0] == 0);
            if not thresholded: break;
            thresholded = \
                (color_image[x][y][1] >= threshold and thresholded_image[x][y][1] == 255) \
                or \
                (threshold >= color_image[x][y][1] and thresholded_image[x][y][1] == 0);
            if not thresholded: break;
            thresholded = \
                (color_image[x][y][2] >= threshold and thresholded_image[x][y][2] == 255) \
                or \
                (threshold >= color_image[x][y][2] and thresholded_image[x][y][2] == 0);
            if not thresholded: break;
        if not thresholded: break;

    assert thresholded;

## Tests the threshold_image_manual function, using a color image and a unconvenient threshold
#
# @param color_image : the color image for the test
def test_threshold_image_numpy_with_unconvenient_threshold(color_image):
    threshold = [100, 125, 150, 123, 145];

    with pytest.raises(ValueError) as verrinfo:
        imgproc_tools.threshold_image_numpy(color_image, threshold);
    assert 'Please provide a convenient threshold value' in str(verrinfo.value);

## Tests the threshold_image_manual function, using a color image and a unconvenient threshold type
#
# @param grayscale_image : the grayscale image for the test
def test_threshold_image_numpy_with_unconvenient_threshold_type(grayscale_image):
    threshold = [100, 125, 150];

    with pytest.raises(ValueError) as verrinfo:
        imgproc_tools.threshold_image_numpy(grayscale_image, threshold);
    assert 'Please provide a convenient threshold value' in str(verrinfo.value);


""" THRESHOLD_COLORS_OPENCV """


## Tests threshold_colors_opencv function, using an empty fixture
#
# @param empty_fixture : the empty fixture for the test
def test_threshold_colors_opencv_with_empty_fixture(empty_fixture):
    with pytest.raises(ValueError) as verrinfo:
        imgproc_tools.threshold_colors_opencv(empty_fixture);
    assert 'Please provide a valid image' in str(verrinfo.value);

## Tests threshold_colors_opencv function, using a grayscale image
#
# @param grayscale_image : the grayscale image for the test
def test_threshold_colors_opencv_with_grayscale_image(grayscale_image):
    threshold, thresholded_image = imgproc_tools.threshold_colors_opencv(grayscale_image);

    thresholded = True;

    for x in xrange(thresholded_image.shape[0] - 1):
        for y in xrange(thresholded_image.shape[0] - 1):
            thresholded = \
                (grayscale_image[x][y] >= threshold and thresholded_image[x][y] == 255) \
                or \
                (threshold >= grayscale_image[x][y] and thresholded_image[x][y] == 0);
            if not thresholded: break;
        if not thresholded: break;

    assert thresholded;

## Tests the threshold_colors_opencv function, using a color image
#
# @param color_image : the color image for the test
def test_threshold_colors_opencv_with_color_image(color_image):
    threshold, thresholded_image = imgproc_tools.threshold_colors_opencv(color_image);

    thresholded = True;

    for x in xrange(thresholded_image.shape[0] - 1):
        for y in xrange(thresholded_image.shape[0] - 1):
            thresholded = \
                (color_image[x][y][0] >= threshold[0] and thresholded_image[x][y][0] == 255) \
                or \
                (threshold[0] >= color_image[x][y][0] and thresholded_image[x][y][0] == 0);
            if not thresholded: break;
            thresholded = \
                (color_image[x][y][1] >= threshold[1] and thresholded_image[x][y][1] == 255) \
                or \
                (threshold[1] >= color_image[x][y][1] and thresholded_image[x][y][1] == 0);
            if not thresholded: break;
            thresholded = \
                (color_image[x][y][2] >= threshold[2] and thresholded_image[x][y][2] == 255) \
                or \
                (threshold[2] >= color_image[x][y][2] and thresholded_image[x][y][2] == 0);
            if not thresholded: break;
        if not thresholded: break;

    assert thresholded;


""" NOTE : When using functions from library imports, tests can't be as accurate as when using hand made functions.
i.e. to be able to check threshold processes on output images with opencv functions, we have to pull back the effective
optimal thresholds computed by the OTSU-y function. The tested function prototype may have to change to allow this...

To display each test execution time, add the argument "--durations=0" to the pytest launch command.
We can thus notice that hierarchy of time consumption : manual > numpy ~ opencv
"""