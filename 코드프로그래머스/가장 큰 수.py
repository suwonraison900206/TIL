def solution(numbers):
    answer = ''

    for i in range(len(numbers)):
        numbers[i] = [str(numbers[i]), str(numbers[i])]

    for i in range(len(numbers)):
        numbers[i][0] = numbers[i][0] * 3
        if int(numbers[i][0]) == 1000:
            numbers[i][0] = 1000
        else:

            numbers[i][0] = numbers[i][0]

    numbers.sort(key=lambda x:x[0], reverse=True)
    print(numbers)

    for i in range(len(numbers)):
        answer = answer + numbers[i][1]
    answer = str(int(answer))
    return answer

numbers = [0, 0]
solution(numbers)

