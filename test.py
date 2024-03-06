import numpy as np

array = np.array([[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]])
padded_array = np.pad(array, ((1, 1), (1, 1)), 'edge')

print(padded_array)
