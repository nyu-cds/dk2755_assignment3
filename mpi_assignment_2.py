
'''
The MPI program is run with different number of processes.  
To start with, the user enter any valid number less than 100. Each process multiply this number by it's rank and pass on
the new value to the next process.
Eventually the single final result of all these mulplication is printed.
'''

import numpy as np
from mpi4py import MPI

#Process info
comm = MPI.COMM_WORLD  #Init communicator
rank = comm.Get_rank() #Get process rank
num_proc = comm.Get_size() #Get total number of processes


if rank == 0:
    while(1):
        user_input = input("\n Enter a valid number less than 100: ") #receive user input
        try:
            value = int(user_input) #check whether the input is of int type
        except:
            print("\n ERROR: The input type is not integer. Please re-enter a valid integer")
            continue   #input is NOT int type and so, re-enter the input
            
        if value >= 100: #check if input value is greater than 100
            print("\n ERROR: The input value is greater than 100. Please re-enter an integer less than 100")
            continue  #input value is greater than 100 and so, re-enter the input          
        else:
            break #valid input and so, continue to the next section
        
    comm.send(value, dest=(rank+1)%num_proc) #send the value to the next process          
    result = comm.recv(source=num_proc - 1) #receive the value from the last process
        
    print("\n The final result received by process 0: ", result) #print the final value recieved from the last process 
            
else:
    recv_val = comm.recv(source=rank-1) #receive the value from the previous process
    print ("\n Received value from process ", rank-1, " is ", recv_val) 
    
    recv_val *= rank #multiply the received value by it's rank
    print (" Sent value from process ", rank, " is ", recv_val)

    if rank == num_proc - 1: 
        comm.send(recv_val, dest=0) #if it's the last process, pass on the mutiplied value to process 0
    else:
        comm.send(recv_val, dest=rank+1) #if it's NOT the last process, pass on the mutiplied value to the next process
        
        

