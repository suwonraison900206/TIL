import sys
from itertools import permutations, combinations
sys.stdin = open('스타트와 링크.txt')

N = int(input())
map_lst = [list(map(int, input().split())) for __ in range(N)]
number_lst = [i for i in range(N)]
result = []
cnt = float('inf')

for i in combinations(number_lst, len(number_lst) // 2):
    b = []
    for j in number_lst:
        if j not in i:
            b.append(j)

    cnt_i = 0
    cnt_b = 0

    for j in permutations(i, 2):
        cnt_i = cnt_i + map_lst[j[0]][j[1]]
    for w in permutations(b, 2):
        cnt_b = cnt_b + map_lst[w[0]][w[1]]

    if abs(cnt_i - cnt_b) < cnt:
        cnt = abs(cnt_i - cnt_b)

print(cnt)
