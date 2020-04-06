import sys
sys.stdin = open("3347.txt")

t = int(input())

for test_case in range(t):
    N, M = list(map(int,input().split()))
    A_list = list(map(int,input().split()))
    B_list = list(map(int,input().split()))

    k = []
    for i in range(len(B_list)):
        for j in range(len(A_list)):
            if A_list[j] <= B_list[i]:
                k.append(j)
                break


    result = [0] * 1001

    for i in range(len(k)):
        result[k[i]] += 1


    q = max(result)

    cnt =0

    for i in range(len(result)):
        if result[i] == q:
            cnt = i


    print('#{} {}'.format(test_case+1, cnt+1))
    #




