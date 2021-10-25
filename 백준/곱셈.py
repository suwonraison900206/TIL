T = int(input())
lst = [list(map(int, input().split())) for _ in range(T)]

for i, (x, y) in enumerate(lst, start=1):
    print('Case #{}: {} + {} = {}'.format(i, x, y, x+y))

