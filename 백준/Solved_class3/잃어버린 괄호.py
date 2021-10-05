
number = list(input().split('-'))
result = []
result2 = 0
print(number)
for i in number:
    cnt = 0
    number2 = i.split('+')

    for j in number2:

        cnt = cnt + int(j)
    result.append(cnt)

for i, v in enumerate(result):

    if i == 0:
        result2 += v
    else:
        result2 -= v
print(result2)