def create_matrix(row, column):
    matrix = []
    for i in range(row):
        input_val = input().split(' ')
        if len(input_val) == column:
            m1 = [int(i) for i in input_val]
            matrix.append(m1)
    return matrix


def print_matrix(matrix):
    print('Output:\n')
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=' ')
        print('')


def matrix_addition(matrix_1, matrix_2):
    sum_matrix = []
    if len(matrix_1) == len(matrix_2) and len(matrix_1[0]) == len(matrix_2[0]):
        for i in range(len(matrix_1)):
            temp = []
            for j in range(len(matrix_1[0])):
                _sum = matrix_1[i][j] + matrix_2[i][j]
                temp.append(_sum)
            sum_matrix.append(temp)
        print_matrix(sum_matrix)
    else:
        print('ERROR')


def matrix_multiplication(matrix, multiplier):
    multi_matrix = []
    for i in range(len(matrix)):
        temp = []
        for j in range(len(matrix[0])):
            result = matrix[i][j] * multiplier
            temp.append(result)
        multi_matrix.append(temp)
    print_matrix(multi_matrix)


r1, c1 = input().split(" ")
matrix_a = create_matrix(int(r1), int(c1))
n = int(input())
matrix_multiplication(matrix_a, n)
