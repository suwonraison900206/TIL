
number = [1] * (123456 * 2 + 1)
number[0], number[1] = 0, 0
for i in range(2, len(number)):

    if number[i] == 1:

        for j in range(2*i, len(number), i):
            number[j] = 0

while True:

    a = int(input())
    if a == 0:
        break
    cnt = 0
    for k in range(a+1, 2*a+1):

        if number[k] == 1:
            cnt +=1
    print(cnt)

