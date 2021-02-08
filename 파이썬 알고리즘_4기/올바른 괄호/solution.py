def solution(s):
    answer = True

    left_flag = 0

    for i in s:
        if i == '(':
            left_flag += 1
        elif i == ')':
            if left_flag == 0:
                return False
            else:
                left_flag -= 1

    return left_flag == 0
    #     if left_flag != 0:
    #         return False
    #
    #     return True
    # 한줄로 대체 가능



s = "()()"
solution(s)



