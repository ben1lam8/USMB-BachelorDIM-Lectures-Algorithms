## @namespace S1_algotools_tests
# A Set to test Algotools functions
# 
# @author Benoit Lamit, LPro DIM, IUT Annecy le vieux, FRANCE

import imp;
import pytest;
import numpy;
import random;

algo_tools = imp.load_source('S1_algotools', 'assignments/Session1/S1_algotools.py');

""" FIXTURES """
@pytest.fixture
def empty_list_fixture():
    return [];

@pytest.fixture
def no_numeric_list_fixture():
    return [True, None, 'c', "Dey"];

@pytest.fixture
def positive_int_list_fixture():
    return [1, 2, 3, 4, 5];

@pytest.fixture
def relative_int_list_fixture():
    return [-1,2,-3,4,-5];

@pytest.fixture
def numeric_list_fixture():
    return [-1.2, 3, -4.5, 6.7, -9];

@pytest.fixture
def complete_list_fixture():
    return [1, 'b', 2.3, "quatre", True, -5.4, False, None];

@pytest.fixture
def empty_matrix_fixture():
    return numpy.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]);

@pytest.fixture
def large_matrix_fixture():
    return numpy.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]);

@pytest.fixture
def medium_matrix_fixture():
    return numpy.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]);

@pytest.fixture
def biased_matrix_fixture():
    return numpy.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]);

@pytest.fixture
def corrupted_matrix_fixture():
    return numpy.array([[0, 0, 0, 0, 0, 0, 0, 0, None, 0],
                        [0, 5, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, False, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 3, 0, 0, 0],
                        [0, 2.3, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, "wow", 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 'a']]);

@pytest.fixture
def char_table_fixture():
    table = numpy.chararray([10,10]);
    table[:] = '';

    return table;

@pytest.fixture
def invalid_table_fixture():
    table = numpy.zeros((10, 10))

    return table;


""" TESTS FOR AVERAGE_ABOVE_ZERO """


## Tests the average_above_zero function, using an empty list fixture
#
# @param empty_list_fixture : the empty list fixture for the test
def test_average_above_zero_with_empty_list_fixture(empty_list_fixture):
    with pytest.raises(ValueError) as verrinfo:
        algo_tools.average_above_zero(empty_list_fixture);
    assert 'No positive value found' in str(verrinfo.value);

## Tests the average_above_zero function, using an no_numeric_list fixture
#
# @param no_numeric_list_fixture : the empty list fixture for the test
def test_average_above_zero_with_no_numeric_list_fixture(no_numeric_list_fixture):
    with pytest.raises(ValueError) as verrinfo:
        algo_tools.average_above_zero(no_numeric_list_fixture);
    assert 'No positive value found' in str(verrinfo.value);

## Tests the average_above_zero function, using a int list fixture
#
# @param positive_int_list_fixture : the int list fixture for the test
def test_average_above_zero_with_positive_int_list_fixture(positive_int_list_fixture):
    result = algo_tools.average_above_zero(positive_int_list_fixture);
    assert result == 3.0;
    
## Tests the average_above_zero function, using a int list fixture
#
# @param relative_int_list_fixture : the int list fixture for the test
def test_average_above_zero_with_relative_int_list_fixture(relative_int_list_fixture):
    result = algo_tools.average_above_zero(relative_int_list_fixture);
    assert result == 3.0;
    
## Tests the average_above_zero function, using a numeric list fixture
#
# @param numeric_list_fixture : the numeric list fixture for the test
def test_average_above_zero_with_numeric_list_fixture(numeric_list_fixture):
    result = algo_tools.average_above_zero(numeric_list_fixture);
    assert result == 4.85;
    
## Tests the average_above_zero function, using a numeric list fixture
#
# @param complete_list_fixture : the complete list fixture for the test
def test_average_above_zero_with_complete_list_fixture(complete_list_fixture):
    result = algo_tools.average_above_zero(complete_list_fixture);
    assert result == 1.65;


""" TESTS FOR MAX_VALUE """


## Tests the max_value function, using an empty list fixture
#
# @param empty_list_fixture : the empty list fixture for the test
def test_max_value_with_empty_list_fixture(empty_list_fixture):
    with pytest.raises(ValueError) as verrinfo:
        algo_tools.max_value(empty_list_fixture);
    assert 'Provided list is empty' in str(verrinfo.value);

## Tests the max_value function, using an no_numeric list fixture
#
# @param no_numeric_list_fixture : the no_numeric list fixture for the test
def test_max_value_with_no_numeric_list_fixture(no_numeric_list_fixture):
    with pytest.raises(ValueError) as verrinfo:
        algo_tools.max_value(no_numeric_list_fixture);
    assert 'No numeric value found' in str(verrinfo.value);

## Tests the max_value function, using a int list fixture
#
# @param positive_int_list_fixture : the int list fixture for the test
def test_max_value_with_positive_int_list_fixture(positive_int_list_fixture):
    result = algo_tools.max_value(positive_int_list_fixture);
    assert result == (5, 4);
    
## Tests the max_value function, using a int list fixture
#
# @param relative_int_list_fixture : the int list fixture for the test
def test_max_value_with_relative_int_list_fixture(relative_int_list_fixture):
    result = algo_tools.max_value(relative_int_list_fixture);
    assert result == (4, 3);
    
## Tests the max_value function, using a numeric list fixture
#
# @param numeric_list_fixture : the numeric list fixture for the test
def test_max_value_with_numeric_list_fixture(numeric_list_fixture):
    result = algo_tools.max_value(numeric_list_fixture);
    assert result == (6.7, 3);
    
## Tests the max_value function, using a numeric list fixture
#
# @param complete_list_fixture : the complete list fixture for the test
def test_max_value_with_complete_list_fixture(complete_list_fixture):
    result = algo_tools.max_value(complete_list_fixture);
    assert result == (2.3, 2);


""" TESTS FOR REVERSE_TABLE """


## Tests the reverse_table function, using an empty list fixture
#
# @param empty_list_fixture : the empty list fixture for the test
def test_reverse_table_with_empty_list_fixture(empty_list_fixture):
    with pytest.raises(ValueError) as verrinfo:
        algo_tools.reverse_table(empty_list_fixture);
    assert 'Provided list is empty' in str(verrinfo.value);


## Tests the reverse_table function, using an no_numeric list fixture
#
# @param no_numeric_list_fixture : the no_numeric list fixture for the test
def test_reverse_table_with_no_numeric_list_fixture(no_numeric_list_fixture):
    result = algo_tools.reverse_table(no_numeric_list_fixture);
    assert result == ["Dey", 'c', None, True];


## Tests the reverse_table function, using a int list fixture
#
# @param positive_int_list_fixture : the int list fixture for the test
def test_reverse_table_with_positive_int_list_fixture(positive_int_list_fixture):
    result = algo_tools.reverse_table(positive_int_list_fixture);
    assert result == [5, 4, 3, 2, 1];


## Tests the reverse_table function, using a int list fixture
#
# @param relative_int_list_fixture : the int list fixture for the test
def test_reverse_table_with_relative_int_list_fixture(relative_int_list_fixture):
    result = algo_tools.reverse_table(relative_int_list_fixture);
    assert result == [-5, 4, -3, 2, -1];


## Tests the reverse_table function, using a numeric list fixture
#
# @param numeric_list_fixture : the numeric list fixture for the test
def test_reverse_table_with_numeric_list_fixture(numeric_list_fixture):
    result = algo_tools.reverse_table(numeric_list_fixture);
    assert result == [-9, 6.7, -4.5, 3, -1.2];


## Tests the reverse_table function, using a numeric list fixture
#
# @param complete_list_fixture : the complete list fixture for the test
def test_reverse_table_with_complete_list_fixture(complete_list_fixture):
    result = algo_tools.reverse_table(complete_list_fixture);
    assert result == [None, False, -5.4, True, "quatre", 2.3, 'b', 1];


""" TESTS FOR ROI_BBOX """


## Tests the roi_bbox function, using an empty matrix fixture
#
# @param empty_matrix_fixture : the empty matrix fixture for the test
def test_roi_bbox_with_empty_matrix_fixture(empty_matrix_fixture):
    with pytest.raises(ValueError) as verrinfo:
        algo_tools.roi_bbox(empty_matrix_fixture);
    assert 'Provided image is empty' in str(verrinfo.value);

## Tests the roi_bbox function, using a large matrix fixture
#
# @param large_matrix_fixture : the large matrix fixture for the test
def test_roi_bbox_with_large_matrix_fixture(large_matrix_fixture):
    result = algo_tools.roi_bbox(large_matrix_fixture);
    assert result == ([1, 1], [8, 1], [8, 8], [1, 8]);

## Tests the roi_bbox function, using a large matrix fixture
#
# @param medium_matrix_fixture : the medium matrix fixture for the test
def test_roi_bbox_with_medium_matrix_fixture(medium_matrix_fixture):
    result = algo_tools.roi_bbox(medium_matrix_fixture);
    assert result == ([3, 3], [6, 3], [6, 6], [3, 6]);

## Tests the roi_bbox function, using a biased matrix fixture
#
# @param biased_matrix_fixture : the biased matrix fixture for the test
def test_roi_bbox_with_biased_matrix_fixture(biased_matrix_fixture):
    result = algo_tools.roi_bbox(biased_matrix_fixture);
    assert result == ([3, 2], [6, 2], [6, 5], [3, 5]);

## Tests the roi_bbox function, using an corrupted matrix fixture
#
# @param corrupted_matrix_fixture : the corrupted matrix fixture for the test
def test_roi_bbox_with_corrupted_matrix_fixture(corrupted_matrix_fixture):
    with pytest.raises(ValueError) as verrinfo:
        algo_tools.roi_bbox(corrupted_matrix_fixture);
    assert 'Provided image is corrupted (a value is not a binary)' in str(verrinfo.value);


""" TESTS FOR RANDOM FILL SPARSE """

## Tests the random_fill_sparse function, using a char_table fixture
#
# @param char_table_fixture : the char table fixture for the test
def test_random_fill_sparse_with_char_table(char_table_fixture):
    vfill = random.randint(0, len(char_table_fixture));
    result = algo_tools.random_fill_sparse(char_table_fixture, vfill);

    rvfill = 0;
    for char in numpy.nditer(result):
        if char == 'X':
            rvfill += 1;

    assert vfill == rvfill;

## Tests the random_fill_sparse function, using a invalid_table fixture
#
# @param invalid_table_fixture : the invalid table fixture for the test
def test_random_fill_sparse_with_invalid_table(invalid_table_fixture):
    vfill = random.randint(0, len(invalid_table_fixture));
    with pytest.raises(ValueError) as verrinfo:
        algo_tools.random_fill_sparse(invalid_table_fixture, vfill);
    assert 'Provided table is of invalid type (numpy.core.defchararray.chararray expected)' in str(verrinfo.value);

## Tests the random_fill_sparse function, using a invalid vfill value
#
# @param char_table_fixture : the char table fixture for the test
def test_random_fill_sparse_with_invalid_vfill(char_table_fixture):
    with pytest.raises(ValueError) as verrinfo:
        algo_tools.random_fill_sparse(char_table_fixture, 0);
    assert 'Why filling with nothing ?' in str(verrinfo.value);


""" TESTS FOR REMOVE WHITESPACE """




""" TESTS FOR SHUFFLE """




""" TESTS FOR SORT SELECTIVE """




""" TESTS FOR SORT BUBBLE """


