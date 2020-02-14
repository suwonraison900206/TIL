t = int(input())

for test_case in range(t):
    a = int(input())
    n = [[0] * a for _ in range(a)]


    dx =[0,1,0,-1]
    dy =[1,0,-1,0]
    direction = 0

    number = 1


    while a * a >= number:


        l_num1 = 0
        l_num2 = -1

        di = l_num1 + dx[direction]
        dj = l_num2 + dy[direction]

    if 0 <= di <= a and 0 <= dj < a and b[di][dj] !=0:
        direction = direction + 1
        if direction == 4:
            direction = 0
    else:
        l_num1 = di
        l_num2 = dj
        n[l_num1][l_num2] = number
        number = number + 1
