def solution(s):
    answer = 0
    half_s = len(s) // 2
    count = 1
    compare = ''
    final_count = []
    real_count = []
    if len(s) != 1:
        for i in range(1, half_s+1):
            stack = []
            for j in range(len(s)):
                try:
                    if len(s[(j * i)::]) != 0:
                        stack.append(s[(j*i): (j*i)+i])
                except:
                    stack.append(s[(j*i)::])
            print(stack)
            for q in range(len(stack)):

                if compare != stack[q]:
                    compare = stack[q]
                    if q+1 < len(stack) and compare == stack[q+1]:
                        count = count + 1
                    else:
                        if count != 1:
                            final_count.append(str(count))
                        final_count.append(compare)
                        count = 1
                else:
                    if q+1 < len(stack) and compare == stack[q+1]:
                        count = count + 1
                    else:
                        if count != 1:
                            final_count.append(str(count))
                        final_count.append(compare)
                        count = 1
            real_count.append(len("".join(final_count)))
            final_count = []

    else:
        answer = 1
        return answer
    print(real_count)
    real_count.sort()
    answer =real_count[0]

    return answer

s = "aaabb"
solution(s)

