def solution(n):
    answer =[]
    def abc(number, n, i):
        print(number)
        if number > n:
            return
        elif number < n:
            abc(number + (i + 1), n, i+1)
        elif number == n:
            print(number, n , i)
            answer.append(1)

    for i in range(1, (n//2) + 1):

        abc(i, n, i)

    print(answer)


    return len(answer) + 1


n = 9999
solution(n)