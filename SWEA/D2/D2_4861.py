import sys
sys.stdin = open("4861.txt")


t = int(input())

for test_case in range(t):
    N , M = map(int,input().split())
    temp1 = []
    for i in range(N):
        temp = list(input())
        temp1.append(temp)
    k = []
    k1 = []
    cnt = 0
    for i in range(N):
        for j in range(N):
            k.append(temp1[i][j])
            if len[k] == M:
                k1 = k[::-1]

                if k == k1 and cnt == 0:
                    cnt = cnt +1
                    print('#{} {}'.format(test_case+1,k))

    k = []
    k1 = []

    for y in range(N):
        for x in range(N):
            k.append(temp1[x][y])
            if len[k] == M:
                k1 = k[::-1]

                if k == k1 and cnt == 0:
                    cnt = cnt +1
                    print('#{} {}'.format(test_case+1,k))

