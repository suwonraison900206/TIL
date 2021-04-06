import sys
sys.stdin = open("9205_맥주 마시면서 걸어가기.txt")

T = int(input())

for __ in range(T):
    N = int(input())
    home = list(map(int,input().split()))
    pyun = []
    for i in range(N):
        pyun.append(list(map(int,input().split())))
    Rock = list(map(int,input().split()))
    check_list = []
    start = []
    while True:
        if not start:
            start_x , start_y = home[0], home[1]
        else:
            start_x, start_y = start.pop()
        if abs(Rock[0] - start_x) + abs(Rock[1] - start_y) <= 1000:
            print('happy')
            break


        for x,y in pyun:
            if abs(x - start_x) + abs(y -start_y) <= 1000 and [x,y] not in check_list:
                check_list.append([x,y])
                start.append([x,y])
            else:
                pass
        if not start:
            print('sad')
            break