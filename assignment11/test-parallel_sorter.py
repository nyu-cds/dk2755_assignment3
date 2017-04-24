
import numpy as np
import unittest
from parallel_sorter import split_limits, split_dataset

class test_functions(unittest.TestCase):

    def set(self):
        pass
    
    def test_split_limits(self):
        print("test_split_limits")
        self.assertEqual(list(split_limits([7, 3, -1, 4, 2, 4, 1, -2, 8], 4)), [-2. ,  0.5,  3. ,  5.5,  8. ])

    def test_split_dataset(self):
        print("test_split_dataset")
        self.assertEqual(split_dataset([7, 3, -1, 4, 2, 4, 1, -2, 8], 4), 
                         [[-1, -2], [3, 2, 1], [4, 4], [7, 8]])

if __name__ == '__main__':
    unittest.main()

