def solution(s):
    cnt = 1
    for i in range(len(s)-1,-1,-1):
        for j in range(len(s) - i + 1, 2, -1 ):
            print(s[i:i + j])
            if len(s[i:i + j]) <= cnt:
                continue
            if s[i:i + j] == s[i:i + j][::-1]:

                if len(s[i:i + j]) > cnt:
                    cnt = len(s[i:i + j])
    return cnt


s = "ecdabbbbdc"
print(solution(s))