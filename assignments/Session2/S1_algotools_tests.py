## @namespace S1_algotools_tests
# A Set to test Algotools functions
# 
# @author Benoit Lamit, LPro DIM, IUT Annecy le vieux, FRANCE

import imp;
algo_tools = imp.load_source('S1_algotools', '../Session1/S1_algotools.py');

#Fixtures :
@pytest.fixture
def int_list_fixture1():
    return [1,2,3,4,-7];

@pytest.fixture
def int_list_fixture2():
    return [-1,2,-20];


def init_test(name, fixture):
    print("Test name : {n}\nTest fixture : {f}".format(n=name, f=fixture));


## Tests the average_above_zero function, using a int list fixture
#
# @param int_list_fixture : the int list fixture for the test
def test_average_above_zero_with_int_list_fixture1(int_list_fixture1):
    init_test(__name__, int_list_fixture1);
    result = algo_tools.average_above_zero(int_list_fixture1);
    assert result == 2.5;

## Tests the max_value function, using a int list fixture
#
# @param int_list_fixture2 : the int list fixture for the test    
def test_max_value_with_int_list_fixture2(int_list_fixture2):
    init_test(__name__, int_list_fixture2);
    result = algo_tools.max_value(int_list_fixture2);
    assert result == 2;
