t = int(input())

for test_case in range(t):
    k = list(map(str,input().split()))
    stack = []
    for i in range(len(k)):
        if k[i] == '*':
            if stack:
                a = stack.pop()
            else:
                print('#{} error '.format(test_case + 1))
                break
            if stack:
                b = stack.pop()
            else:
                print('#{} error '.format(test_case + 1))
                break
            result = int(b) * int(a)
            stack.append(result)

        elif k[i] == '/':
            if stack:
                a = stack.pop()
            else:
                print('#{} error '.format(test_case + 1))
                break
            if stack:
                b = stack.pop()
            else:
                print('#{} error '.format(test_case + 1))
                break
            result = int(b) / int(a)
            stack.append(result)

        elif k[i] == '+':
            if stack:
                a = stack.pop()
            else:
                print('#{} error '.format(test_case + 1))
                break
            if stack:
                b = stack.pop()
            else:
                print('#{} error '.format(test_case + 1))
                break
            result = int(b) + int(a)
            stack.append(result)

        elif k[i] == '-':
            if stack:
                a = stack.pop()
            else:
                print('#{} error '.format(test_case + 1))
                break
            if stack:
                b = stack.pop()
            else:
                print('#{} error '.format(test_case + 1))
                break
            result = int(b) - int(a)
            stack.append(result)

        elif k[i] == '.':
            if len(stack) == 1:
                a = stack.pop()
                print('#{} {}'.format(test_case+1,int(a)))
                break
            else:
                print('#{} error '.format(test_case + 1))
                break
        else:
            stack.append(k[i])

