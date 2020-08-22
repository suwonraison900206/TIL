#-*- coding: utf-8 -*-
import sys , copy
sys.stdin = open("개리맨더링.txt", 'rt', encoding='UTF8')

def line(index, map):
    pass



N = int(input())

map_lst = [list(map(int,input().split())) for __ in range(N)]
map_lst2 = [[0] * N for __ in range(N)]

for i in range(N):
    for j in range(N):
        if (i == 0 and j == 0) or (i == N-1 and j == N-1) or (i == N-1 and j == 0) or (i == 0 and j == N-1):
            pass
        else:
            copy_map = copy.deepcopy(map_lst2)
            k = i + j
            for x in range(k, N):
                for y in range(k, N):
                    print(i, j , x,y)

                print('****')
            print('&&&&&')



