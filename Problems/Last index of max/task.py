def last_indexof_max(numbers):
    # write the modified algorithm here
    temp = 0
    for i, num in enumerate(numbers):
        if temp <= num:
            temp = num
            index = i
        else:
            continue
    return index

print(last_indexof_max([8, 11, 15, 15, 15, 12]))