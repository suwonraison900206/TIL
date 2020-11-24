import sys
sys.stdin = open("컨베이어벨트.txt")

N, K = map(int, input().split())

belt_lst = list(map(int,input().split()))

cnt = 1
K_count = 0

belt_lst2 = [0] * len(belt_lst)
robot_lst = [0] * len(belt_lst)
robot_lst2 = [0] * len(belt_lst)


while True:

    K_count = 0

    for i in range(len(belt_lst)):  # 1. 벨트가 한칸 회전한다

        if i == len(belt_lst)-1:
            belt_lst2[0] = belt_lst[i]
        else:
            belt_lst2[i+1] = belt_lst[i]

    for i in range(len(robot_lst)):

        if i == len(robot_lst)-1:
            robot_lst2[0] = robot_lst[i]
        else:
            robot_lst2[i+1] = robot_lst[i]

    belt_lst = belt_lst2[:]
    robot_lst = robot_lst2[:]

    if robot_lst[N-1] == 1:
        robot_lst[N-1] = 0

    for i in range(len(robot_lst)-1, -1, -1):  #2
        if robot_lst[i] == 1:
            if robot_lst[i+1] == 1:
                pass
            elif belt_lst[i+1] == 0:
                pass
            else:
                robot_lst[i+1] = 1
                robot_lst[i] = 0
                belt_lst[i+1] = belt_lst[i+1] - 1

    if robot_lst[N - 1] == 1:
        robot_lst[N - 1] = 0

    if belt_lst[0] != 0: # 3
        if robot_lst[0] == 0:
            robot_lst[0] = 1
            belt_lst[0] = belt_lst[0] - 1

    for i in range(len(belt_lst)):

        if belt_lst[i] == 0:
            K_count = K_count + 1

    if K_count >= K:
        break
    cnt = cnt + 1

    print(belt_lst)



print(cnt)


