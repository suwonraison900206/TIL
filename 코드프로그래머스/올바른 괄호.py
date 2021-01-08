def solution(s):
    answer = True

    left_flag = 0
    right_flag = 0

    for i in range(len(s)):
        if s[i] == '(':
            left_flag +=1
        elif s[i] == ')':
            if left_flag == 0:
                return False
            else:
                left_flag -= 1
    if left_flag !=0:
        return False
    else:
        return True


s = "(()("

print(solution(s))