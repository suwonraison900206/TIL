def solution(n):
    ans = 0
    print(n)
    while n !=1:
        print(n)
        if n % 2 == 0:
            n = n // 2
        elif n % 2 == 1:
            n = n -1
            n = n //2
            ans += 1
    print(ans)
    return ans

n = 5000
solution(n)