'''
The MPI program prints 2 different statements based on it's rank value
'''

from mpi4py import MPI

comm = MPI.COMM_WORLD #Init communicator
rank = comm.Get_rank() #Get the process rank from the communicator

#Check whether the rank is odd or even
if rank%2 == 0:  
    print("Hello from process ", rank) #even rank
else:
    print("Goodbye from process ", rank) #odd rank
    


