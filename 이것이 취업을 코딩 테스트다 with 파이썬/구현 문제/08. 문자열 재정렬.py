import sys
sys.stdin = open("08. 문자열 재정렬.txt")

S = list(map(str,input()))

number_sum = 0
str_lst = []

for i in range(len(S)):
    try:
        number_sum = number_sum + int(S[i])
    except:
        str_lst.append(S[i])

str_lst.sort()
str_lst.append(str(number_sum))
print("".join(str_lst))
