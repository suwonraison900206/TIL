def solution(s):
    word = []  # 변수명은 직관적인 이름으로 짓자

    for i in s:

        while word and word[-1] < i:
            word.pop()

        word.append(i)

    return ''.join(word)