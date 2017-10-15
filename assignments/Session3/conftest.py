## @namespace conftest
# A set of fixtures for the tests for the generic functions for image management
# Please do not rename. Pytest wouldn't find fixtures anymore.
#
# @author Benoit Lamit, LPro DIM, IUT Annecy le vieux, FRANCE

import pytest;
import cv2;

@pytest.fixture
def empty_fixture():
    return None;

@pytest.fixture
def grayscale_image():
    return cv2.imread('assignments/Session3/myimage.jpg',0);

@pytest.fixture
def color_image():
    return cv2.imread('assignments/Session3/myimage.jpg',1);