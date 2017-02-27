
import itertools
from itertools import permutations

def zbits(n,k):
    '''
    n - length of the binary strings required to be generated 
    k - number of zeros in the binary string
    '''
    
    #VALIDATE THE INPUT VALUES
    if (type(n) != int) or (type(k) != int) :
        print "ERROR: One or both the inputs are NOT integers"
        return
    elif (n < 0) or (k < 0):
        print "ERROR: One or both the inputs are negative"
        return 
    elif n < k:
        print "ERROR: n is less than k"
        return 
    
    #GENERATE A SET OF STRINGS OF BINARY VALUES OF LENGTH n WITH k NUMBER OF ZEROS IN THEM
    bVal = '0'*k + '1'*(n-k)    
    strBinary = {''.join(s) for s in permutations(bVal, n)}
    
    return strBinary


#VALIDATE THE 'zbits' FUNCTION
if __name__ == '__main__':    

    assert zbits(4, 3) == {'0100', '0001', '0010', '1000'}
    assert zbits(4, 1) == {'0111', '1011', '1101', '1110'}
    assert zbits(5, 4) == {'00001', '00100', '01000', '10000', '00010'}  


