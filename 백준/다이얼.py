
word = list(str(input()))
cnt = 0
for i in word:

    if 65 <= ord(i) <= 67:
        cnt += 3
    elif 68 <= ord(i) <= 70:
        cnt += 4
    elif 71 <= ord(i) <= 73:
        cnt += 5
    elif 74 <= ord(i) <= 76:
        cnt += 6
    elif 77 <= ord(i) <= 79:
        cnt += 7
    elif 80 <= ord(i) <= 83:
        cnt += 8
    elif 84 <= ord(i) <= 86:
        cnt += 9
    elif 87 <= ord(i) <= 90:
        cnt += 10
print(cnt)