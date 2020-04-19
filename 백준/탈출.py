import sys
sys.stdin = open("escape.txt")

R, C = map(int,input().split())
lst = []
for i in range(R):
    lst.append(list(input()))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
stack1 = []
stack1_1 = []

stack2 = []
stack2_2 = []

count = 0
result = 0
for i in range(R):
    for j in range(C):
        if lst[i][j] == 'S':
            stack1.append((i,j))
        elif lst[i][j] == '*':
            stack2.append((i,j))


while stack2 or stack1:
    if result == 0 and len(stack2) != 0:
        water = stack2.pop()
        for i in range(4):
            di = water[0] + dx[i]
            dj = water[1] + dy[i]
            if 0 <= di <= (R-1) and 0 <= dj <= (C-1) and lst[di][dj] == '.':
                lst[di][dj] = '*'
                stack2_2.append((di,dj))
    elif result == 1:
        break
    if len(stack2) == 0:
        while stack1:
            stone = stack1.pop()
            for i in range(4):
                di = stone[0] + dx[i]
                dj = stone[1] + dy[i]
                if 0 <= di <= (R-1) and 0 <= dj <= (C-1) and lst[di][dj] == '.':
                    lst[di][dj] = 'S'
                    lst[di-dx[i]][dj-dy[i]] = '.'
                    stack1_1.append((di,dj))
                elif 0 <= di <= (R-1) and 0 <= dj <= (C-1) and lst[di][dj] == 'D':
                    result = result + 1
                    count = count + 1
                    break
            if result == 0 and len(stack1) == 0:
                count = count + 1
                stack2 = stack2_2[:]
                stack1 = stack1_1[:]
                stack2_2 = []
                stack1_1 = []
                break
            else:
                break
if result == 1:
    print(count)
else:
    print('KAKTUS')










