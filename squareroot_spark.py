'''
Spark program to calculate the average of the square root of all the numbers from 1 to 1000. 
'''

from pyspark import SparkContext
import numpy as np
from operator import add

if __name__ == '__main__':
    sc         = SparkContext("local", "averageSquareroot")
    avg_sqroot = sc.parallelize(range(1, 1001)).map(lambda x: np.sqrt(x)).fold(0, add)
    print("Average square roots: ", avg_sqroot/1000)
