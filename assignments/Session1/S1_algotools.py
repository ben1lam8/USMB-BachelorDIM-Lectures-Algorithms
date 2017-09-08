## @namespace S1_algotools
# A set of generic functions for data management
# 
# @author Benoit Lamit, LPro DIM, IUT Annecy le vieux, FRANCE

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
#
# @param input_list : an array of values
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

## Returns the highest value of a list
# 
# @param input_list : the input list to be scanned
# @return the highest value in the input list, its index in the input list
# @throws an exception (ValueError) on an empty list
def max_value(input_list):
    
    #first, check if provided list is not empty
    if len(input_list)==0:
        raise ValueError('Provided list is empty');
    
    #if not, init max_val and its index
    max_val=input_list[0];
    max_idx=0;
    
    """
    #iterate on range
    for idx in range(len(input_list)):
        #select only positive items
        if max_val<input_list[idx]:
            max_val=input_list[idx];
            max_idx=idx;
    """
            
    #iterate on enumeration
    for idx, item in enumerate(input_list):
        #select only positive items
        if max_val<item:
            max_val=item;
            max_idx=idx;
            
            
    return max_val, max_idx;

"""
#testing max_value function :

#test1 : basic test (expected answer=2)
mylist=[-1,2,-20]

mymax, mymaxidx=max_value(mylist);
print('Max value of {input_list} is ({max_scan}, {max_index})'.format(input_list=mylist, max_scan=mymax, max_index=mymaxidx));
#==> message : "Max value of [-1, 2, -20] is (2, 1)"

mymax_tuple=max_value(mylist);
mymax=mymax_tuple[0];
print('Max value of {input_list} is {max_scan}'.format(input_list=mylist, max_scan=mymax));
#==> message : "Max value of [-1, 2, -20] is 2"

#test2 : error test (Exception expected)
max_value([]);
#==> message : ... "provided list is empty" ...
"""

## Returns the reversed array
#
# @param input_list : the array to be reversed
# @return the reversed array
def reverse_table(input_list):
    
    #first, check if provided list is not empty
    if len(input_list)==0:
        raise ValueError('Provided list is empty');
    
    #if not, return a reversed array with slice syntax   
    return input_list[::-1];

"""
#testing reverse_table function :

#test1 : basic test (exepected answer=[65, 92, 15, 14, 3])
mylist=[3, 14, 15, 92, 65];

myreversedlist = reverse_table(mylist);
print('Input list : {input} | Reversed list {output}'.format(input=mylist, output=myreversedlist));
#==> message : "Input list : [3, 14, 15, 92, 65] | Reversed list : [65, 92, 15, 14, 3]"

#test2 : error test (Exception expected)
reverse_table([]);
#==> message : ... "provided list is empty" ...
"""
