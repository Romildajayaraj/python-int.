def add_matrices(matrix1, matrix2):
    # Get the number of rows and columns
    rows = len(matrix1)
    cols = len(matrix1[0])

    # Initialize the result matrix with zeros
    result = []

    # Loop through rows
    for i in range(rows):
        row = []
        # Loop through columns
        for j in range(cols):
            # Add corresponding elements
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)

    return result
mat1 = [
    [1, 2, 3],
    [4, 5, 6]
]

mat2 = [
    [7, 8, 9],
    [1, 2, 3]
]

# Add matrices
sum_matrix = add_matrices(mat1, mat2)

# Display result
print("Resultant Matrix:")
for row in sum_matrix:
    print(row)
