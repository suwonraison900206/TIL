
def solution(s):
    answer = 0
    result = []

    if len(s) == 1: # 입력값 길이가 1인 경우, 테스트5번
        return 1

    for i in range(1,(len(s)//2) + 1):
        stack = []
        for j in range(0, len(s), i): # 1 ~ 입력값의 절반 길이까지 슬라이싱
            stack.append(s[j:j+i])

        cnt = 1
        flag = False
        final_stack = []

        for alpha in stack:

            if flag == False:
                flag = alpha
            else:
                if flag == alpha: # 앞에꺼와 같다면 카운트값 올려줌
                    cnt = cnt + 1
                else:
                    if cnt != 1: # 카운트가 1이 아니면 카운트와 겹친 문자열 저장

                        final_stack.append(str(cnt)) # join 쓸때 에러떠서 문자열로 바꿔서 넣었습니다.
                        final_stack.append(flag)
                        flag = alpha
                        cnt = 1
                    else:
                        final_stack.append(flag)
                        flag = alpha
                        cnt = 1
        if cnt == 1:
            final_stack.append(flag)
        else:
            final_stack.append(str(cnt))
            final_stack.append(flag)

        result.append(len(''.join(final_stack))) # 결과 값 길이 저장

    return min(result)

s = "abcabcabcabcdededededede"
solution(s)