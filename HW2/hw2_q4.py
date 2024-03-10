"""Create a 4x4 NumPy array filled with random integers between 1 and 100. Then, 
reshape this array into two separate 2D arrays, where one represents the rows and 
the other represents the columns. Write a  lambda function, to calculate the sum 
of each row and each column separately, and return the results as two separate 
NumPy arrays"""

import numpy as np
import pandas as pd

array = np.random.randint(1, 100, 16).reshape(4, 4)
print(array)

rows = array.reshape(2, 8)
print(rows)
columns = array.reshape(8,2)

rowSum = lambda arr: np.sum(arr, axis=1)
sumColumn = lambda arr: np.sum(arr, axis=0)

rowResult = rowSum(rows)
rowColumn = sumColumn(columns)

print(rowResult)
print(rowColumn)
