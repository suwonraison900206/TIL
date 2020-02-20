a = '2+3*4/5'

operator = ['*', '/']
operator1 =['+', '-']
stack = []

cnt = 0

for i in a:
    if i in operator:
        if cnt == 0:
            if stack[-1] in operator1:
                k = stack[-1]
                stack.pop()
                stack.append(i)
                stack.append(k)
                cnt += 1
        elif cnt == 1:
            if stack in operator:
                k = stack[-1]
                print(k, end='')
                if stack in operator:
                    stack.pop()
    elif i in operator1:
        stack.append(i)
    else:
        print(i, end='')

