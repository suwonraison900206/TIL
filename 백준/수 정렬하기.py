N = int(input())
lst = [int(input()) for _ in range(N)]
lst.sort()
for number in lst:
    print(number)