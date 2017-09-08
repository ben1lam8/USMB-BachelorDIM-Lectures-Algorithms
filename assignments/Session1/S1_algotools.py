##
#
# @author Benoit Lamit, LPro DIM, IUT Annecy le vieux, FRANCE
# @brief a set of generic functions for data management

"""
# a variable
a=1; # default type : int

# an empty list
mylist = [];

#a filled list
mylist2=[1,2,3];

#append to a list
mylist.append(10);

# a buggy list
mybuggylist=[1,'a', "Hi"];

#operators
b=a+2;
mylist_sum=mylist+mylist2;
"""

## Compute the average of positive elements in a list
# @param input_list an array of values
# @return the computed average
def average_above_zero(input_list):
    
    #init critical variable
    positive_values_sum=0;
    positive_values_count=0;
    
    #compute the average of positive elements of a list
    for item in input_list:
        #select only positive items
        if item>0:
            positive_values_sum+=item;
            positive_values_count+=1;
        elif item==0:
            print('This value is null:'+str(item));
        else:
            print('This value is negative:'+str(item));
            
    #compute the final average
    average=float(positive_values_sum)/float(positive_values_count);
    print('Positive elements average is '+str(average));
    
    return float(average);

"""
#testing average_above_zero function:

mylist=[1,2,3,4,-7];
result=average_above_zero(mylist);

message='The average of positive samples of {list_value} is {res}'.format(list_value=mylist,
                                                                          res=result);
print(message);
"""


def max_value(input_list):
    ##
    # basic function able to return the max value of a list
    # @param input_list : the input list to be scanned
    # @throws an exception (ValueError) on an empty list
    
    #first check if provided list is not empty
    if len(input_list)==0:
        raise ValueError('provided list is empty')
    #init max_value and its index
    max_val=input_list[0]
    max_idx=0
    #compute the average of positive elements of a list
    """for item in input_list:
        #select only positive items
        if max_val<item:
            max_val=item
    """
    #generic style : iterate over the range of list indexes 
    for idx in range(len(input_list)):
        #select only positive items
        if max_val<input_list[idx]:
            max_val=input_list[idx]
            max_idx=idx
            
    
    #generic style : iterate over the range of list indexes 
    for idx, item in enumerate(input_list):
        #select only positive items
        if max_val<item:
            max_val=item
            max_idx=idx
            
            
    return max_val, max_idx
"""
#test max_value function
#1 basic test, expected answer=2
mylist=[-1,2,-20]
mymax, mymaxidx=max_value(mylist)
mymax_tuple=max_value(mylist)
mymax=mymax_tuple[0]
print('Max value of {input_list} is {max_scan}'.format(input_list=mylist, max_scan=mymax))
#==> message : "Max value of [-1, 2, -20] is (2, 1)"

#2 error test : Exception expected 
max_value([])
"""