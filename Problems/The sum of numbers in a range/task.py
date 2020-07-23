def range_sum(numbers, start, end):
    _sum = 0
    for n in numbers:
        if start <= n <= end:
            _sum += n
    return _sum



input_numbers =  [int(n) for n in input().split(" ")]
a, b = map(int, input().split(" "))
print(range_sum(input_numbers, a, b))