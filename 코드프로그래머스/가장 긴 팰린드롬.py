def solution(s):
    cnt = 1
    for i in range(len(s)):
        for j in range(2, len(s)-i+1):
            if s[i:i+j] == s[i:i+j][::-1]:
                if len(s[i:i+j]) > cnt:
                    cnt = len(s[i:i+j])
    return cnt