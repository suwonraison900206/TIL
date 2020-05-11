import sys
sys.stdin = open('경사로.txt','r')

N, L = map(int,input().split())

map_lst = [list(map(int,input().split())) for __ in range(N)]
ladder_lst1 =[[0] * N for __ in range(N)]
ladder_lst2 =[[0] * N for __ in range(N)]
print(ladder_lst1)

k = 0
result = 2 * N

for i in range(N): # 가로 탐색
    flag = 0
    count = 1
    for j in range(N-1):
        if flag == 1:
            break
        else:
            if map_lst[i][j] == map_lst[i][j+1]:
                count = count + 1
            elif map_lst[i][j] - map_lst[i][j+1] == 1:
                for k in range(j+1, N-1):
                    if map_lst[i][k] == map_lst[i][k+1]:
                        if ladder_lst1[i][k] == 0 and ladder_lst1[i][k+1] != 1:
                            ladder_lst1[i][k] = 1
                        else:
                            flag = 1
                            break  # 실패
                    else:
                        flag = 1
                        break # 실패
            elif map_lst[i][j] - map_lst[i][j + 1] == -1:
                if count >= L: # 성공
                    count = 1
                else:  # 실패
                    flag = 1
                    break

            elif abs(map_lst[i][j] - map_lst[i][j + 1] ) == 2: # 실패
                flag = 1


    if flag == 1:
        result = result - 1

print(result)



