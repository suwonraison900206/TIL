

def divide(N, x, y):
    global lst
    if N == 1:
        lst[x][y] = '*'
    else:
        new_N = N // 3

        for dx in range(3):
            for dy in range(3):
                if dx != 1 or dy != 1:
                    divide(new_N, x+ dx * new_N, y + dy * new_N)

N = int(input())
lst = [[' '] * N for _ in range(N)]

divide(N, 0, 0)

for w in lst:
    print(''.join(w))