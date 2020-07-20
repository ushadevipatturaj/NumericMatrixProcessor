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
    matrix = [([0] * column) for _ in range(row)]
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


def matrix_transpose(matrix, type_char):
    new_matrix = []
    if type_char == 1:
        new_matrix = create_zero_matrix(len(matrix), len(matrix[0]))
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                new_matrix[i][j] = matrix[j][i]
    elif type_char == 2:
        for i in range(len(matrix) - 1, -1, -1):
            temp = []
            for j in range(len(matrix[0]) - 1, -1, -1):
                temp.append(matrix[j][i])
            new_matrix.append(temp)
    elif type_char == 3:
        for i in range(len(matrix)):
            temp = []
            for j in range(len(matrix[0]) - 1, -1, -1):
                temp.append(matrix[i][j])
            new_matrix.append(temp)
    elif type_char == 4:
        for i in range(len(matrix) - 1, -1, -1):
            temp = []
            for j in range(len(matrix[0])):
                temp.append(matrix[i][j])
            new_matrix.append(temp)
    print_matrix(new_matrix)


def play():
    run = True
    while run:
        print("\n1. Add matrices\n2. Multiply matrix by a constant\n3. Multiply matrices\n"
              "4. Transpose matrix\n0. Exit\n")
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
        elif play_choice == 4:
            print("\n1. Main diagonal\n2. Side diagonal\n3. Vertical line\n4. Horizontal line")
            transpose_type = int(input("Your choice:"))
            matrix = create_matrix("")
            matrix_transpose(matrix, transpose_type)


play()
