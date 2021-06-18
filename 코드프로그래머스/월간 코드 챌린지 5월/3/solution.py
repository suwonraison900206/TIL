def solution(s):
    answer = []

    for number in s:
        cnt = 0
        stack =[]
        for num in number:
            if int(num) == 1:
                stack.append(num)
            elif int(num) == 0:
                if len(stack) >= 2:
                    if int(stack[-1]) == 1 and int(stack[-2]) == 1:
                        cnt +=1
                        stack.pop()
                        stack.pop()
                    else:
                        stack.append(num)
                else:
                    stack.append(num)
        print(stack, cnt)

        if len(stack) >= 3:

            if stack[-1] == '1' and stack[-2] == '1' and stack[-3] == '1':
                answer.append(''.join(stack[:len(stack) - 3]) + ('110' * cnt) + '111')
            else:
                for i in range(len(stack) - 1, -1, -1):
                    if stack[i] == '0':
                        a = stack[:i + 1]
                        b = stack[i + 1:]
                        c = ''.join(a) + ('110' * cnt) + ''.join(b)
                        answer.append(c)
                        break

        else:
            zero_count =[]
            one_count = []

            for i in range(len(stack)):

                if stack[i] == '0':
                    zero_count.append(i)
                elif stack[i] == '1':
                    one_count.append(i)

            if len(zero_count) == 0:
                answer.append(('110' * cnt) +''.join(stack))
            else:
                answer.append(''.join(stack) + ('110' * cnt))

    print(answer)
    return answer

s = ["1110","100111100","0111111010"]
solution(s)