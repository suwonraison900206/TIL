import sys
sys.stdin = open("5102.txt")

T = int(input())

for test_case in range(T):
    V, E = map(int,input().split())

    lst = []

    for i in range(E):
        lst.append(list(map(int,input().split())))

    final = list(map(int,input().split()))

    visited_lst = [[0] * (V+1) for __ in range(V+1)]

    stack = []
    stack2 = []
    stack.append(final[0])
    count = 1
    result = 0

    while stack:
        K = stack.pop()
        for i in range(len(lst)):
            if lst[i][0] == K and visited_lst[K][lst[i][1]] == 0:
                if lst[i][1] == final[1]:
                    print('#{} {}'.format(test_case+1,count))
                    result +=1
                    break
                else:
                    visited_lst[K][lst[i][1]] = 1
                    visited_lst[lst[i][1]][K] = 1
                    stack2.append(lst[i][1])

            if lst[i][1] == K and visited_lst[lst[i][0]][K] == 0:
                if lst[i][0] == final[1]:
                    print('#{} {}'.format(test_case+1,count))
                    result += 1
                    break
                else:
                    visited_lst[K][lst[i][0]] = 1
                    visited_lst[lst[i][0]][K] = 1
                    stack2.append(lst[i][0])
        if result != 0:
            break
        if len(stack) == 0:
            stack = stack2
            stack2 = []
            count = count +1
    if result == 0:
        print('#{} 0'.format(test_case+1))