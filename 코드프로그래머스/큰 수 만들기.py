def solution(number, k):
    number = list(number)

    while k != 0:
        if min(number) == 9:
            break
        flag = 0
        for i in range(0, len(number)-1):

            if number[i] < number[i + 1]:
                number.pop(i)
                k -= 1
                flag = 1
                break
        if flag == 0:
            break

    return ''.join(number[0:len(number) - k])
number = "9999"
k = 3
print(solution(number, k))