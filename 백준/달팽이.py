n = int(input())
number = int(input())
count = n**2

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
lst = [[0] * n for _ in range(n)]
check = 0
start = [[0, 0]]

while start:

    x, y = start.pop()
    lst[x][y] = count
    count -= 1
    if count == 0:
        break

    if -1 < x + dx[check] < n and -1 < y + dy[check] < n and lst[x + dx[check]][y + dy[check]] == 0:

        start.append([x + dx[check], y + dy[check]])
    else:
        check += 1
        if check == 4:
            check = 0
        start.append([x + dx[check], y + dy[check]])

for i in lst:
    print(*i)

for i in range(n):
    for j in range(n):

        if lst[i][j] == number:
            print(i+1, j+1)
            