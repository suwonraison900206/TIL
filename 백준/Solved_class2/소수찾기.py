N = int(input())
numbers = list(map(int,input().split()))
cnt = 0
for number in numbers:

    if number == 1:
        continue
    elif number == 2:
        cnt +=1
    else:

        for i in range(2, int(number ** 0.5) +1):

            if number % i == 0:
                break
        else:
            cnt += 1
print(cnt)

