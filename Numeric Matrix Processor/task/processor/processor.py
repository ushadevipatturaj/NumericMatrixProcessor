def create_matrix(number):
    row, column = map(int, input("Enter size of {} matrix:".format(number)).split(" "))
    print("Enter {} matrix:".format(number))
    matrix = []
    for i in range(row):
        input_val = input().split(' ')
        if len(input_val) == column:
            m1 = [int(i) if '.' not in i else float(i) for i in input_val]
            matrix.append(m1)
    return matrix


def create_zero_matrix(row, column):
    matrix = [([0]*column) for i in range(row)]
    return matrix

def print_matrix(matrix):
    print('The result is:')
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
        print('The operation cannot be performed.\n')


def matrix_multiplication_with_constant(matrix, multiplier):
    multi_matrix = []
    for i in range(len(matrix)):
        temp = []
        for j in range(len(matrix[0])):
            result = matrix[i][j] * multiplier
            temp.append(result)
        multi_matrix.append(temp)
    print_matrix(multi_matrix)

def matrices_multiplication(matrix_1, matrix_2):
    if len(matrix_1[0]) == len(matrix_2):
        result_matrix = create_zero_matrix(len(matrix_1), len(matrix_2[0]))
        for i in range(len(matrix_1)):
            for j in range(len(matrix_2[0])):
                for k in range(len(matrix_2)):
                    result_matrix[i][j] += matrix_1[i][k] * matrix_2[k][j]
        print_matrix(result_matrix)
    else:
        print('The operation cannot be performed.\n')

def play():
    run = True
    while run:
        print("1. Add matrices\n2. Multiply matrix by a constant\n3. Multiply matrices\n0. Exit\n")
        play_choice = int(input("Your choice:"))
        if play_choice == 0:
            run = False
            exit(0)
        elif play_choice == 1:
            matrix_a = create_matrix("first")
            matrix_b = create_matrix("second")
            matrix_addition(matrix_a, matrix_b)
        elif play_choice == 2:
            matrix_a = create_matrix("")
            n = input('Enter constant:')
            n = int(n) if '.' not in n else float(n)
            matrix_multiplication_with_constant(matrix_a, n)
        elif play_choice == 3:
            matrix_a = create_matrix("first")
            matrix_b = create_matrix("second")
            matrices_multiplication(matrix_a, matrix_b)
play()
