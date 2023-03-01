# Matrix is a way to describe 2D list. an array with another array inside of it.
# Simple example of 3*3 matrix

simple_matrix = [
    [4,3,5],
    [3,2,9],
    [4,2,5]
]

# To access the value, we go row to columns respectively.
# The following prints, the value that is found in the second index row and second index column
# which is the third row and the third column = 5

print(simple_matrix[2][2])