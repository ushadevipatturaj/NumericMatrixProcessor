def last_indexof_max(numbers):
    # write the modified algorithm here
    temp = 0
    index = 0
    for n in range(len(numbers)):
        if temp <= numbers[n]:
            temp = numbers[n]
            index = n
        else:
            continue
    return index

# print(last_indexof_max([8, 11, 15, 15, 15, 12]))