T = int(input())

numbers = [int(input()) for __ in range(T)]
result = [0] * 41
result[0] = 1
result[1] = 1

for i in range(2, len(result)):
    result[i] = result[i-2] + result[i-1]

for number in numbers:
    zero = []
    one = []

    if number == 0:
        print(1, 0)
    elif number == 1:
        print(0, 1)
    elif number == 2:
        print(1, 1)
    else:
        print(result[number-2], result[number-1])