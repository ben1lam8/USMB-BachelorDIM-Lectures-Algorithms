## @namespace S1_algotools
# A set of generic functions for data management
# 
# @author Benoit Lamit, LPro DIM, IUT Annecy le vieux, FRANCE

import logging;
import numpy;
import random;
from __builtin__ import int

#Logger configuration. Choose one :

LOG_LEVEL = logging.DEBUG;
#LOG_LEVEL = logging.INFO;
#LOG_LEVEL = logging.WARN;
#LOG_LEVEL = logging.ERROR;
#LOG_LEVEL = logging.CRITICAL;

logger = logging.getLogger('logger');
logger.setLevel(LOG_LEVEL);

ch = logging.StreamHandler();
ch.setLevel(LOG_LEVEL);

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s');

ch.setFormatter(formatter);

logger.addHandler(ch);


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
        
        #check for type compatibility
        if type(item) is None:
            print('This value is empty : {v}'.format(v=str(item)));
            continue;
        
        if type(item) not in [int,float]:
            print('This value is not numeric : {v}'.format(v=str(item)));
            continue;
        
        #select only positive items
        if item>0:
            positive_values_sum+=item;
            positive_values_count+=1;
        elif item==0:
            print('This value is null : {v}'.format(v=str(item)));
        else:
            print('This value is negative : {v}'.format(v=str(item)));
            
    #check for correct computation
    if positive_values_count==0: raise ValueError("No positive value found");
    
    #compute the final average
    average=float(positive_values_sum)/float(positive_values_count);
    print('Positive elements average is {a}'.format(a=average));
    
    return float(average);

## Returns the highest value of a list
# 
# @param input_list : the input list to be scanned
# @return the highest value in the input list, its index in the input list
# @throws an exception (ValueError) on an empty list
def max_value(input_list):
    
    #first, check if provided list is not empty
    if len(input_list)==0:
        raise ValueError('Provided list is empty');
    
    #check for first valid index
    first_valid_index = 0;
    
    while (first_valid_index < len(input_list)) and (type(input_list[first_valid_index]) is None or type(input_list[first_valid_index]) not in [int, float]):
        first_valid_index += 1;
        
    if first_valid_index == len(input_list): raise ValueError("No numeric value found");
    
    #if checked, init max_val and its index
    max_val=input_list[first_valid_index];
    max_idx=first_valid_index;    
            
    #iterate on enumeration
    for idx, item in enumerate(input_list):
        
        #check for type compatibility
        if type(item) is None:
            print('This value is empty : {v}'.format(v=str(item)));
            continue;
        
        if type(item) not in [int,float]:
            print('This value is not numeric : {v}'.format(v=str(item)));
            continue;
        
        #select only positive items
        if max_val<item:
            max_val=item;
            max_idx=idx;
            
            
    return max_val, max_idx;

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
    
    #switch values using a temp variable
    for i in xrange(0, halfLength) :
        temp = input_list[i];
        input_list[i] = input_list[length-1-i];
        input_list[length-1-i] = temp;

    return input_list;

## Returns the coordinates of the minimum bounding box corners corresponding to the input array/image
#
# @param input_image : the binary array/image to be bounded
# @return an array of the coordinates of the minimum bounding box
def roi_bbox(input_image):
    
    #first, check if provided image is not blank
    if len(input_image) == 0:
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
            if type(input_image[row][col]) is numpy.int_ and input_image[row][col] == 1:
                oned_points.append([row, col]);
            elif type(input_image[row][col]) is not numpy.int_:
                raise ValueError('Provided image is corrupted (a value is not a binary)');

    #check if provided image is not empty
    if len(oned_points) == 0: raise ValueError('Provided image is empty');
                
    #if not, update the bounds
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

## Fills a square matrix with a chosen number of 'X' characters
#
# @param table : the square matrix to fill
# @param vfill : the number of Xs to insert
# @return the filled array
def random_fill_sparse(table, vfill):

    #check if params are valid
    if type(table) is not numpy.core.defchararray.chararray:
        raise ValueError('Provided table is of invalid type (numpy.core.defchararray.chararray expected)');
    if vfill == 0 :
        raise ValueError('Why filling with nothing ?');

    #generate lucky coordinates for Xs
    xs_abs = [];
    
    while len(xs_abs) != vfill:
        abs = random.randint(0, table.shape[0]-1);
        if abs in xs_abs: continue;
        xs_abs.append(abs);
        
    xs_ord = [];
    
    while len(xs_ord) != vfill:
        ord = random.randint(0, table.shape[1]-1);
        if ord in xs_ord: continue;
        xs_ord.append(ord);
    
    #insert Xs into the table
    for i in xrange(len(xs_abs)):
        table[xs_abs[i]][xs_ord[i]] = 'X';
    
    return table;

## Removes whitespaces inside a string
#
# @param table : the string to clean
# @return the cleaned string
def remove_whitespace(table):
    
    #first, check if provided string is valid
    if type(table) is not str:
        raise ValueError('Only strings can be processed');

    if len(table)==0:
        raise ValueError('Provided string is empty');
    
    #if not, return a cleaned string...
    """
    #1 | Single line cheated solution
    
    return table.replace(' ', '');
    """
    
    """
    #2 | Asked solution... maybe
    
    #python strings are immutable...
    #we need to "parse" it into an array
    parsed_table = list(table);

    non_space_chars = 0;
    
    for char in parsed_table:
        if char != ' ': 
            parsed_table[non_space_chars] = char;
            non_space_chars += 1;
            
    #the cleaned parsed table now needs to be trimmed
    #is there another option but slice ?
    parsed_table = parsed_table[:non_space_chars];
    
    return ''.join(parsed_table);
    """
    
    #"""
    #3 | Another array-free solution :
    #(potential memory leaks because of amounts of generated strings)
    
    cleaned_table = "";
    
    for char in table:
        if char != ' ':
            cleaned_table += char;
    
    return cleaned_table;
    #"""

## Shufffles an input list in a memory-friendly way
#
# @param list_in : the input_list to shuffle
# @return the shuffled list
def shuffle(list_in):
    logger.info("Function {func} called".format(func=shuffle.__name__));
    logger.debug("Parameters : {lin}".format(lin=list_in));
    
    #Store indexes to be randomized
    unselected_indexes = range(0, len(list_in));
    
    #Abracadabra !
    for i in xrange(len(list_in)):

        logger.debug("Remaining indexes to process : {ui}".format(ui=unselected_indexes));
        logger.debug("Working on {ind}th index".format(ind=i));
        
        if not unselected_indexes or i not in unselected_indexes : 
            logger.debug("This index has already been processed. Skipping it...\n");
            continue;
        
        logger.debug("This index hasn't been processed yet !");
            
        unselected_indexes.remove(i);
        logger.debug("This index won't be processed another time.");
        
        #Get a lucky value amongst remaining indexes
        logger.debug("Getting a lucky other index...");
        rand = random.choice(unselected_indexes);
        logger.debug("Lucky index : {rd}".format(rd=rand));
        unselected_indexes.remove(rand);
        logger.debug("This index won't be processed another time.");
        
        logger.debug("Switching {idx}th and {rd}th values...".format(idx=i, rd=rand));
        temp = list_in[i];
        list_in[i] = list_in[rand];
        list_in[rand] = temp;
        logger.debug("Values switched !\n");
    
    logger.debug("All indexes have been processed.");     
    return list_in;

"""
#testing shuffle function :

#test1 : basic test
mylist=map(chr, range(97, 123));

myshuffledlist=shuffle(mylist);
print('Input list : \n{input} \n Output shuffled list : \n{output}'.format(input=mylist, output=myshuffledlist));
"""

"""
Exercice 9 : selective sort
(a) Illustrate the algorithm on the following vector sample : 10, 15, 7, 1, 3, 3, 9
(b) Does the number of iterations depend on the vector content ?
(c) How many iterations are required to sort the whole vector ?
(d) How many permutations are applied ?
(e) How many comparisons are applied ?
(f) Can you quantify the algorithm complexity ?
(g) compare the number of permutations and comparisons for input vectors of varying sizes : 50, 100 and 500
"""

## Sorts a list in the ascending order using the selective sort algorithm
#
# @param list_in : the list to be sorted
# @return the sorted list
def sort_selective(list_in):
    
    #Work on a clone list:
    list_out = list(list_in);
    
    #Iterate trough all indexes
    for i in xrange(len(list_out)):
        
        #Consider the current index' value as the smallest
        index_of_smallest = i;
        
        #If a smaller value is found inside the remaining values, tag its index
        for j in xrange(i, len(list_out)):
            if list_out[j] < list_out[index_of_smallest]:
                index_of_smallest = j;
        
        #Switch the tagged value with the one at the current index
        temp = list_out[index_of_smallest];
        list_out[index_of_smallest] = list_out[i];
        list_out[i] = temp;
        
    return list_out;

"""
#testing sort_selective function :

#test1 : basic test
mylist=list([10,15,7,1,3,3,9]);

mysortedlist=sort_selective(mylist);
print('Input list : \n{input} \nOutput sorted list : \n{output}'.format(input=mylist, output=mysortedlist));
"""

"""
Exercice 9 : bubble sort
(a) Illustrate the algorithm on the following vector sample : 10, 15, 7, 1,3, 3, 9
(b) Does those number of iterations depend on the vector content ?
(c) How many iterations are required to sort the whole vector ?
(d) How many permutations are applied ?
(e) How many comparisons are applied ?
(f) Can you quantify the algorithm complexity ?
(g) compare the number of permutations and comparisons for input vectors of varying sizes : 50, 100 and 500
"""
    
## Sorts a list in the ascending order using the bubble sort algorithm
#
# @param list_in : the list to be sorted
# @return the sorted list
def sort_bubble(list_in):
    
    #Work on a clone list
    list_out = list(list_in);
    
    #Consider the list to be sorted shorter each time
    for i in reversed(xrange(len(list_out))):
        
        #Swap values if needed, until the considered top limit of the list
        for j in xrange(i):
            if list_out[j] > list_out[j+1]:
                
                temp = list_out[j];
                list_out[j] = list_out[j+1];
                list_out[j+1] = temp;
    
    return list_out;

"""
#testing sort_bubble function :

#test1 : basic test
mylist=list([10,15,7,1,3,3,9]);

mysortedlist=sort_bubble(mylist);
print('Input list : \n{input} \nOutput sorted list : \n{output}'.format(input=mylist, output=mysortedlist));
"""

