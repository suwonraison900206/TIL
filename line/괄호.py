def solution(inputString):
    count = 0
    lst = []

    k = 1

    for i in range(len(inputString)):
        lst.append(inputString[i])


    stack = []
    while k == 1:
        cnt = 0
        for i in range(len(lst)):
            if lst[i] == '(':
                stack.append(i)
                for j in range(len(lst)):
                    if lst[j] == ')':
                        if j > stack[0]:
                            count = count + 1
                            lst.pop(i)
                            lst.pop(j-1)
                            stack.pop(0)
                            cnt = cnt +1

                            break
                break
            elif lst[i] == '{':
                stack.append(i)
                for j in range(len(lst)):
                    if lst[j] == '}':
                        if j > stack[0]:
                            count = count + 1
                            lst.pop(i)
                            lst.pop(j-1)
                            stack.pop(0)
                            cnt = cnt +1

                            break
                break
            elif lst[i] == '[':
                stack.append(i)
                for j in range(len(lst)):
                    if lst[j] == ']':
                        if j > stack[0]:
                            count = count + 1
                            lst.pop(i)
                            lst.pop(j-1)
                            stack.pop(0)
                            cnt = cnt +1

                            break
                break
            elif lst[i] == '<':
                stack.append(i)
                for j in range(len(lst)):
                    if lst[j] == '>':
                        if j > stack[0]:
                            count = count + 1
                            lst.pop(i)
                            lst.pop(j-1)
                            stack.pop(0)
                            cnt = cnt +1

                            break

        if cnt == 0:
            k = k + 1
            break

    if len(stack) == 0:
        print(count)
        return count
    else:
        return -1


k = '))(('

solution(k)



