def solution(s):
    answer = 0
    half_s = len(s) // 2

    print(s)
    count = 1
    stack = []
    for i in range(1, half_s+1):
        print(i)
        for j in range(len(s)):
            try:
                stack.append(s[i+j:(2*i)+j])
            except:
                pass

        print(stack)






    return answer


s = "aabbaccca"

solution(s)

