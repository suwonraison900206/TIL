import sys
sys.stdin = open("02.곱하기 혹은 더하기.txt")

S = list(map(int,input()))

result = 0

for i in range(len(S)-1):
    if (S[i] == 0 or S[i+1] == 0) and result == 0:
        if i == 0:
            result = S[i] + S[i+1]
        else:

            result = result + S[i+1]
    else:
        if i == 0:
            result = S[i] * S[i+1]
        else:
            result = result * (S[i+1])

print(result)