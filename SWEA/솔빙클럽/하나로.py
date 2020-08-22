import sys
sys.stdin = open("하나로.txt")

T = int(input())

for test_case in range(1, T+1):

    N = int(input())

    X_lst = list(map(int,input().split()))
    Y_lst = list(map(int,input().split()))
    E = float(input())
    standard = [X_lst[0], Y_lst[0]]

    codeness =[]

    for i in range(len(X_lst)):

        codeness.append([X_lst[i], Y_lst[i], ((X_lst[i]**2) + (Y_lst[i]**2))])

    codeness.sort(key=lambda x: x[2])
    count = 0
    result = 0
    number = 0
    stack = []
    q = codeness.pop(0)
    stack.append(q)
    while codeness:
        min_v = 1000000000000000000000000000000000000
        for i in range(len(stack)):
            for j in range(len(codeness)):
                number = (abs(stack[i][0] - codeness[j][0]) ** 2) + (abs(stack[i][1] - codeness[j][1]) ** 2)
                if number < min_v:
                    min_v = number
                    codeness[j][2] = min_v

        codeness.sort(key=lambda x:x[2])
        count = count + codeness[0][2]
        k = codeness.pop(0)
        stack.append(k)

    print('#{} {}'.format(test_case, round(count * E)))

    # stack.append(k)
    # print('#{} {}'.format(test_case, round(count)))




