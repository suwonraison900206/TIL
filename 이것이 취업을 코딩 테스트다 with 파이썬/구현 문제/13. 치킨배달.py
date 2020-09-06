from itertools import combinations
import sys
sys.stdin = open("13. 치킨배달.txt")

N, M = map(int,input().split())

city = [list(map(int,input().split())) for __ in range(N)]

house= []
chicken = []

for i in range(len(city)):
    for j in range(len(city)):
        if city[i][j] == 1:
            house.append((i,j))
        elif city[i][j] == 2:
            chicken.append((i, j))
# print(house)
# print(chicken)

ken_lst = list(combinations(chicken, M))
print(ken_lst)

final_lst = []
for i in range(len(ken_lst)):
    result = []
    for q in range(M):
        stack = []
        for j in range(len(house)):
            cnt =abs(house[j][0] - ken_lst[i][q][0]) + abs(house[j][1] - ken_lst[i][q][1])
            # print(cnt)

            stack.append(cnt)
            print(stack)
        result.append(min(stack))
        # print(result)
    print(result)
    final_lst.append(sum(result))
# print(len(ken_lst))
print(ken_lst)
# print(house)
# print(stack)
# print(result)
# print(final_lst)
#
#     print(cnt)
#     result.append(cnt)
# print(result)