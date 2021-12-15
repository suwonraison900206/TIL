n = int(input())
lst = [list(map(int,input().split())) for _ in range(n)]
cnt = 0
check = 0
result = []
dir = 0

for x, y in lst:

    if check == 0:
        result.append([y])
        check = y
    else:

        if x < result[dir][-1]:

            for i in range(len(result)):
                if x < result[i][-1]:
                    continue
                else:
                    result[i].append(y)
                    check = y
                    break

            else:
                result.append([y])
                check = y
                dir += 1

        else:
            result[dir].append(y)

print(result)
print(len(result))
