import sys
sys.stdin = open("5099.txt")

t = int(input())

for test_case in range(t):
    N , M = map(int,input().split())
    C = list(map(int,input().split()))
    number = 1
    count = 0
    stack = []
    stack.append([C.pop(0), 0, number])
    while count == 0:

        for i in range(len(stack)):
            stack[i][1] = stack[i][1] + 1
        for i in range(len(stack)):
            if stack[i][1] == N:
                stack[i][0] = (stack[i][0] // 2)
                stack[i][1] = 0
                if stack[i][0] == 0:
                    if len(C) != 0:
                        number += 1
                        stack.insert(i,[C.pop(0), 0, number])
                        stack.pop(i+1)
                        if len(stack) == 1:
                            print('#{} {}'.format(test_case+1,stack[0][2]))
                            count = count + 1
                            break
                    else:
                        stack.pop(i)
                        if len(stack) == 1:
                            print('#{} {}'.format(test_case+1,stack[0][2]))
                            count = count + 1
                            break
                        else:
                            break
        if len(stack) != N:
            if len(C) != 0:
                number += 1
                stack.append([C.pop(0), 0, number])













