
'''
Original file runtime: 1.215 seconds
Modified file runtime: 0.006 seconds
Speedup = 1.215 / 0.006 = 202.5 

_______________________________________________________________________________________________

1) 'cProfile' OUTPUT
--------------------


a) Original file:
-----------------

1004015 function calls in 1.215 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        2    0.600    0.300    0.608    0.304 <ipython-input-24-656c48a730f4>:22(multiply)
        1    0.247    0.247    0.314    0.314 <ipython-input-24-656c48a730f4>:37(sqrt)
        1    0.000    0.000    1.215    1.215 <ipython-input-24-656c48a730f4>:50(hypotenuse)
        1    0.289    0.289    0.293    0.293 <ipython-input-24-656c48a730f4>:9(add)
        1    0.000    0.000    1.215    1.215 <string>:1(<module>)
  1000000    0.063    0.000    0.063    0.000 {math.sqrt}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        4    0.002    0.000    0.002    0.000 {numpy.core.multiarray.zeros}
     4004    0.014    0.000    0.014    0.000 {range}



b) Modified file:
-----------------

3 function calls in 0.006 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.006    0.006    0.006    0.006 <ipython-input-25-d12b44968cec>:8(hypotenuse)
        1    0.000    0.000    0.006    0.006 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

___________________________________________________________________________________________________

2) 'line_profile' OUTPUT
------------------------

The execution time of each lines of the modified 'hypotenuse' function took less time compared to 
the execution time of each lines of the original 'hypotenuse' function. This shows that the in-built 
numpy multiply, add and sqrt functions are faster than our original user defined funcitons.

____________________________________________________________________________________________________

NOTE: Tried using the numpy in-built function 'np.hypot'. But it takes 0.021 seconds which is more 
than the time taken(0.006 seconds) by this modified function.

'''

# ---------------------------------------------------------------
# calculator.py
# ---------------------------------------------------------------
import numpy as np


def hypotenuse(x,y):
    """
    Return sqrt(x**2 + y**2) for two arrays, a and b.
    x and y must be two-dimensional arrays of the same shape.
    """
    xx = np.multiply(x,x)
    yy = np.multiply(y,y)
    zz = np.add(xx, yy)
    return np.sqrt(zz)


# -----------------------------------------------------------------
# calculator_test.py
# -----------------------------------------------------------------

M = 10**3
N = 10**3

A = np.random.random((M,N))
B = np.random.random((M,N))

hypotenuse(A,B)


