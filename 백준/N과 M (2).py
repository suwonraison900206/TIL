from itertools import combinations

N, M = map(int,input().split())
lst = [i for i in range(1, N +1)]
result = []
if M == 1:
    for i in lst:
        print(i)
else:
    for i in combinations(lst, M):

        for j in i:
            print(j, end= ' ')
        print()