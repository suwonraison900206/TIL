import sys
from collections import defaultdict

input = sys.stdin.readline

N, M, B = map(int, input().split())
dic = defaultdict(int)

for i in range(N):
    for j in list(map(int, input().split())):
        dic[j] += 1

key = list(dic.keys())

min_value = min(key)
max_value = max(key)

min_count = int(1e9)
h = 0

for x in range(min_value, max_value + 1):
    count, have = 0, B
    for y in dic.keys():
        if x > y:
            count += (x - y) * dic[y]
            have -= (x - y) * dic[y]
        elif x < y:
            count += 2 * (y - x) * dic[y]
            have += (y - x) * dic[y]

    if have >= 0:
        min_count = min(min_count, count)
        if min_count == count:
            h = x
print(min_count, h)