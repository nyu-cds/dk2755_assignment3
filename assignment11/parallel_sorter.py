
'''
This MPI program generates 10000 random numbers between the range -100 and 10000. The process 0 splits the dataset into different subsets based on the number of processes.
The process 0 then sents the subsets to other processes each of which sorts it's subset. Once done, the sorted subsets are sent back to process 0 which then cancatenates
the sorted subsets to produce the final completed sorted numbers. 
'''

import numpy as np
from mpi4py import MPI

RANDOM_NUM_MIN_LIMIT = -100 # Min int for the random numbers 
RANDOM_NUM_MAX_LIMIT = 10000 # Max int for the random numbers 

comm = MPI.COMM_WORLD  #Initialize MPI communicator
rank = comm.Get_rank() #Get the rank of the processes
size = comm.Get_size() #Get number of processes


def gen_random_numbers():    
    return [np.random.randint(RANDOM_NUM_MIN_LIMIT,RANDOM_NUM_MAX_LIMIT) for i in range(RANDOM_NUM_MAX_LIMIT)]

def split_limits(random_num, size):
    return np.linspace(np.min(random_num),np.max(random_num), num=size+1)

def split_dataset(random_num, size):    
    #Generate data set split limits
    split_limit = split_limits(random_num, size)
    print("\nsplit limits")
    print(split_limit)
    
    #Split the dataset
    dataSplits = list() 
    range_min = np.min(random_num)
    for i in range(0, size):
        range_max = int(split_limit[i+1])+1
        dataSplits.append([x for x in random_num if x in range(range_min, range_max)])
        range_min = range_max
    return dataSplits


dataSplits = None
if rank == 0:    
    #Generate random numbers between RANDOM_NUM_MIN_LIMIT and RANDOM_NUM_MAX_LIMIT
    random_num = gen_random_numbers()

    #Split different set of random numbers based on the above split limits
    dataSplits = split_dataset(random_num, size)
   
    
#Scatter data to different processes other than process 0
dataSplits = comm.scatter(dataSplits, root=0)

#Sort the individual data sets
perProcSort = np.sort(dataSplits)

#Gather the sorted data sets by process 0
sortSet = comm.gather(perProcSort, root=0)

#Concatenate the individual sorted list to a single sorted list by process with rank = 0
if rank == 0:
    completeSort = np.concatenate(sortSet)
    print("\nSorted List")
    print(completeSort) 

