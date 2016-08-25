def determinant(matrix):
    """This script computes the determinant of an n_by_n matrix. Expansion by first row."""
    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        return det
    else:
        sum = 0
        for i in range(len(matrix[0])):
            sum += (-1) ** i * matrix[0][i] * determinant(minor_exp(i, matrix))
        return sum
def minor_exp(column, matrix):
    """This function computes the minor \
    of a matrix."""
    i = 1
    new_matrix = []
    while i < len(matrix):
        temp_matrix = []
        for j in range(len(matrix)):
          if j != column:
            temp_matrix.append(matrix[i][j])
        new_matrix.append(temp_matrix)
        i += 1
    return new_matrix
