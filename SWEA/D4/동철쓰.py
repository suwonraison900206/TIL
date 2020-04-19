# import sys
# sys.stdin = open("dongchul.txt")


def backtrack(a, k, N):
    c = [0] * N

    if k == N:
        lst.append(a[:])
    else:
        in_perm = [False] * N
        for i in range(k):
            in_perm[a[i]] = True

        ncandidates = 0
        for i in range(N):
            if in_perm[i] == False:
                c[ncandidates] = i
                ncandidates += 1

        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k+1, N)







t = int(input())

for test_case in range(t):
    num = int(input())
    k = []
    for i in range(num):
        temp = list(map(int,input().split()))
        k.append(temp)


    lst = []
    a = [0] * num
    backtrack(a, 0, num)
    final_lst = [0]
    max_k = 0

    for i in range(len(lst)):
        sum = 1
        for j in range(num):
            if k[lst[i][j]][j] == 0:
                break
            else:
                sum = (sum * (k[lst[i][j]][j]/100))
                if sum < final_lst[-1]:
                    break

        final_lst.append(sum)


    max_k = max(final_lst) * 100
    print('#{} {:.6f}'.format(test_case+1, max_k))



