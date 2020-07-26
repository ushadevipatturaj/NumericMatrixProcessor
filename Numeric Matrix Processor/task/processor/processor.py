import math

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
            if result == 0.0:
                temp.append(0)
            else:
                temp.append(result)
        multi_matrix.append(temp)
    return multi_matrix



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
    return new_matrix


def matrix_determinant(matrix):
    if len(matrix) >= 2 and len(matrix[0]) >= 2:
        return find_cofactor(matrix)
    else:
        return matrix[0][0]


def find_cofactor(matrix):
    determinant = 0
    if len(matrix) == 2 and len(matrix[0]) == 2:
        determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        for i in range(len(matrix[0])):
            temp = matrix[0][i]
            cofactor_matrix = []
            for x in range(len(matrix)):
                inner = []
                for y in range(len(matrix[0])):
                    if x == 0:
                        continue
                    if y == i:
                        continue
                    elif x != 0 and y != i:
                        inner.append(matrix[x][y])
                if len(inner) > 0:
                    cofactor_matrix.append(inner)
            determinant += pow(-1, i) * (temp * find_cofactor(cofactor_matrix))
    return determinant


def find_adjoint(matrix):
    inverse_cofactor = []
    if len(matrix) == 2 and len(matrix[0]) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        for i in range(len(matrix)):
            temp_cofactor = []
            for j in range(len(matrix[0])):
                temp = matrix[i][j]
                cofactor_matrix = []
                for x in range(len(matrix)):
                    inner = []
                    for y in range(len(matrix[0])):
                        if x == i:
                            continue
                        if y == j:
                            continue
                        elif x != i and y != j:
                            inner.append(matrix[x][y])
                    if len(inner) > 0:
                        cofactor_matrix.append(inner)
                determinant = pow(-1, i) * find_adjoint(cofactor_matrix)
                temp_cofactor.append(determinant)
            inverse_cofactor.append(temp_cofactor)
    return inverse_cofactor


def matrix_inverse(matrix):
    if len(matrix) <= 2 and len(matrix[0]) <= 2:
        print("This matrix doesn't have an inverse.")
        return 0
    else:
        determinant = matrix_determinant(matrix)
        if determinant == 0:
            print("This matrix doesn't have an inverse.")
            return 0
        cofactor = find_adjoint(matrix)
        transposed_cofactor = matrix_transpose(cofactor, 1)
        print(transposed_cofactor)
        quotient = round(1.00 / determinant, 7)
        multiplier = math.floor(abs(quotient) * 10 ** 4) / 10 ** 4
        if quotient < 0:
            multiplier = multiplier * -1
        print(quotient, determinant, quotient)
        return matrix_multiplication_with_constant(transposed_cofactor, multiplier)


def play():
    run = True
    while run:
        print("\n1. Add matrices\n2. Multiply matrix by a constant\n3. Multiply matrices\n"
              "4. Transpose matrix\n5. Calculate a determinant\n6. Inverse matrix\n0. Exit\n")
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
            multi_matrix = matrix_multiplication_with_constant(matrix_a, n)
            print_matrix(multi_matrix)
        elif play_choice == 3:
            matrix_a = create_matrix("first")
            matrix_b = create_matrix("second")
            matrices_multiplication(matrix_a, matrix_b)
        elif play_choice == 4:
            print("\n1. Main diagonal\n2. Side diagonal\n3. Vertical line\n4. Horizontal line")
            transpose_type = int(input("Your choice:"))
            matrix = create_matrix("")
            new_matrix = matrix_transpose(matrix, transpose_type)
            print_matrix(new_matrix)
        elif play_choice == 5:
            matrix = create_matrix("")
            determinant = matrix_determinant(matrix)
            print("The result is:\n", determinant, sep="")
        elif play_choice == 6:
            matrix = create_matrix("")
            inverse_matrix = matrix_inverse(matrix)
            print_matrix(inverse_matrix)


play()
