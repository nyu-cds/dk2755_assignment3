'''
Spark program to count the number of distinct words in the input text. 
'''

from pyspark import SparkContext
import re

# remove any non-words and split lines into separate words
# finally, convert all words to lowercase
def splitter(line):
    line = re.sub(r'^\W+|\W+$', '', line)
    return map(str.lower, re.split(r'\W+', line))

if __name__ == '__main__':
    sc             = SparkContext("local", "countdistinctwords")
    input_file     = sc.textFile('pg2701.txt')
    distinct_words = input_file.flatMap(splitter).distinct().count()
    print("Number of distinct words in the file: ", distinct_words)

