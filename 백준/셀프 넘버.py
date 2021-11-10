number = [i for i in range(1, 10001)]
L = len(number)

for i in range(L):
    if number[i] != 0:
        start = number[i]
    else:
        continue

    while True:
        str_start = list(str(start))
        cnt = 0

        for w in str_start:

            cnt = cnt + int(w)

        start += cnt
        if start > 10000:
            break

        if number[start-1] !=0:
            number[start - 1] = 0

        else:
            break
for i in number:
    if i !=0:
        print(i, end=' ')