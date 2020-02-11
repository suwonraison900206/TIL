
a = []
b = []
for i in range(4):
    a = []
    for j in range(4):
        a.append(0)
    b.append(a)


direction_list = [(0, 1), (1, 0), (0, -1), (-1, 0)]
direction = 0

l_num1 = 0
l_num2 = -1
number = 1

while 4 * 4 >= number:
    dir = direction_list[direction]
    x = l_num1 + dir[0]
    y = l_num2 + dir[1]

    if x < 0 or y < 0 or x >= 4 or y >= 4 or b[x][y] != 0:
        direction = direction + 1
        if direction == 4:
            direction = 0
    else:
        l_num1 = x
        l_num2 = y
        b[l_num1][l_num2] = number
        number = number + 1


print(b)


