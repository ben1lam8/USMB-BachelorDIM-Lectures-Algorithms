
import imp;

algo_tools = imp.load_source('S1_algotools', 'assignments/Session1/S1_algotools');

mylist=[1,2,3,4,-7];
result=algo_tools.average_above_zero(mylist);
