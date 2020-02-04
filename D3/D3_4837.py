arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
n = len(arr)

T = int(input())
for test_case in range(T):
    result = 0
    temp = list(map(int, input().split()))

    for i in range(1<<n):
        cnt = 0
        sum = 0
        for j in range(n+1):
            if i & (1<<j):

                sum = sum + arr[j]
                cnt = cnt + 1
        if cnt == temp[0] and sum == temp[1]:
            result = result + 1

    print('#{} {}'.format(test_case + 1, result))
