#Ex 5

#NumPy Array Manipulation

import numpy as np 

mat = np.arange(1,26).reshape(5,5)

diag = np.diagonal(mat)

diag_sum = np.sum(diag)


print("Matrix: \n", mat)
print("Diagonal elements: \n", diag)
print("Diagonal sum: ", diag_sum)


"""

This program creates a 5x5 NumPy matrix with values from 1 to 25.

It then extracts the diagonal elements of the matrix.

Finally, it calculates and prints the sum of those diagonal elements.

"""