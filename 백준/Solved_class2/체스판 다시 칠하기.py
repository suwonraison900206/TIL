

N, M = map(int,input().split())
chess = [list(input()) for __ in range(N)]

cnt = 0
cnt2 = 0
check1 = ['B', 'W']
check2 = ['W', 'B']
flag = 0

result = []

for ii in range(0,N-7):
    for jj in range(0, M-7):
        cnt = 0
        for i in range(ii, ii+8):
            for j in range(jj, jj+8):
             
                if check1[flag] == chess[i][j]:
                    pass

                elif check1[flag] != chess[i][j]:
                    cnt +=1

                if flag == 1:
                    flag = 0
                else:
                    flag +=1

            if flag == 1:
                flag = 0
            else:
                flag +=1
        result.append(cnt)

for ii in range(0,N-7):
    for jj in range(0, M-7):
        cnt = 0
        for i in range(ii, ii+8):
            for j in range(jj, jj+8):

                if check2[flag] == chess[i][j]:
                    pass

                elif check2[flag] != chess[i][j]:
                    cnt +=1

                if flag == 1:
                    flag = 0
                else:
                    flag +=1

            if flag == 1:
                flag = 0
            else:
                flag +=1
        result.append(cnt)




print(min(result))
# print(cnt, cnt2)