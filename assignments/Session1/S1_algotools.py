## @namespace S1_algotools
# A set of generic functions for data management
# 
# @author Benoit Lamit, LPro DIM, IUT Annecy le vieux, FRANCE

import numpy;

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
    
    #if not, return a reversed array
    length = len(input_list);
    halfLength = length//2; #whole division
    
    #work on a clone list
    output_list = list(input_list); 
    
    #switch values using a temp variable
    for i in xrange(0, halfLength) :
        temp = output_list[i];
        output_list[i] = output_list[length-1-i];
        output_list[length-1-i] = temp;

    return output_list;

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

## Returns the coordinates of the minimum bounding box corners corresponding to the input array/image
#
# @param input_image : the binary array/image to be bounded
# @return an array of the coordinates of the minimum bounding box
def roi_bbox(input_image):
    
    #first, check if provided image is not blank
    if len(input_image)==0:
        raise ValueError('Provided image is blank');
    
    #if not, seek for bounds
    #init the bounds to coordinates around the input image
    min_x = input_image.shape[0];
    max_x = -1;
    min_y = input_image.shape[1];
    max_y = -1;
    
    #read the input image and list the 1-ed points coordinates    
    oned_points = [];
    
    for row in xrange(input_image.shape[0]):
        for col in xrange(input_image.shape[1]):
            if input_image[row][col] == 1:
                oned_points.append([row, col]);
                
    #update the bounds
    for point in oned_points:
        if point[0] < min_x:
            min_x = point[0];

        if point[0] > max_x:
            max_x = point[0];

        if point[1] < min_y:
            min_y = point[1];

        if point[1] > max_y:
            max_y = point[1];
            

    #return the bounds
    return ([min_x, min_y],[max_x, min_y],[max_x,max_y],[min_x,max_y]);
        
"""
#testing roi_bbox function :

#test1 : basic test (random input, unexpected answer... )
myimage=numpy.random.randint(2, size=(10, 10)); #...not a handy test...

mybounds=roi_bbox(myimage);
print('Input image : \n{input} \n Output bounds : {output}'.format(input=myimage, output=mybounds));
#==> message : ... Output bounds : ([0, 0], [9, 0], [9, 9], [0, 9])
"""

## Fills an array with a random number of 'X' characters
#
# @param table : the array to fill
# @param vfill : ?????????????????
# @return the filled array
def random_fill_sparse(table, vfill):
    
    #generate a random binary matrix to spot the 'X's
    xs_positions = numpy.random.randint(2, size=(table.shape[0], table.shape[1]));
    
    #place 'X's inside the table where the 1s are in the matrix
    for row in xrange(table.shape[0]):
        for col in xrange(table.shape[1]):
            if xs_positions[row][col] == 1:
                table[row][col]='X';
            else:
                table[row][col]='';
    
    return table;
    
"""
#testing random_fill_sparse function :

#test1 : basic test (unexpected answer)
mytable=numpy.chararray([10,10]);

myfilledtable=random_fill_sparse(mytable, 0);
print('Input table : \n{input} \n Output filled table : \n{output}'.format(input=mytable, output=myfilledtable));
"""
