## @namespace S1_algotools_tests
# A Set to test Algotools functions
# 
# @author Benoit Lamit, LPro DIM, IUT Annecy le vieux, FRANCE

import imp;
import pytest;
from boto.kinesis.exceptions import InvalidArgumentException
algo_tools = imp.load_source('S1_algotools', 'assignments/Session1/S1_algotools.py');

""" FIXTURES """
@pytest.fixture
def empty_list_fixture():
    fix = ();
    return list(fix);

@pytest.fixture
def positive_int_list_fixture():
    fix = (1,2,3,4,5)
    return list(fix);

@pytest.fixture
def relative_int_list_fixture():
    fix = (-1,2,-3,4,-5);
    return list(fix);

@pytest.fixture
def numeric_list_fixture():
    fix = (-1.2, 3, -4.5, 6.7, -9)
    return list(fix);

@pytest.fixture
def complete_list_fixture():
    fix = (1, 'b', 2.3, "quatre", -5.4, None);
    return list(fix);


""" TESTS FOR AVERAGE_ABOVE_ZERO """

## Tests the average_above_zero function, using an empty list fixture
#
# @param empty_list_fixture : the empty list fixture for the test
def test_average_above_zero_with_empty_list_fixture(empty_list_fixture):
    with pytest.raises(ValueError) as verrinfo:
        algo_tools.average_above_zero(empty_list_fixture);
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
# @param numeric_list_fixture : the numeric list fixture for the test
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
# @param numeric_list_fixture : the numeric list fixture for the test
def test_max_value_with_complete_list_fixture(complete_list_fixture):
    with pytest.raises(ValueError) as verrinfo:
        algo_tools.max_value(empty_list_fixture);
    assert 'No numeric value found' in str(verrinfo.value);

