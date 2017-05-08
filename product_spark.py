'''
Spark program to calculate the product of all the numbers from 1 to 1000 (1000!)
'''

from pyspark import SparkContext
from operator import mul

if __name__ == '__main__':
    sc            = SparkContext("local", "numberFactorial")
    num_factorial = sc.parallelize(range(1, 1001)).fold(1, mul)
    print("The value of 1000!: ", num_factorial)

