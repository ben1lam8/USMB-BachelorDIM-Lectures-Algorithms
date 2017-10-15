## @namespace S3_imgproc_tests
# A set of tests for the generic functions for image management
#
# @author Benoit Lamit, LPro DIM, IUT Annecy le vieux, FRANCE

import imp;
import pytest;

imgproc_tools = imp.load_source('S3_imgproc_tools', 'assignments/Session3/S3_imgproc_tools.py');

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