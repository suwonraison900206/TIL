from collections import Counter


N = int(input())
lst = [int(input()) for _ in range(N)]
lst.sort()

number_dict = {}
for n in lst:
    if n not in number_dict:
        number_dict[n] = 1
    else:
        number_dict[n] += 1
lst2 = []
for key,value in number_dict.items():
    lst2.append([key, value])
lst2.sort(key=lambda x:(-x[1], x[0]))
print(round(sum(lst) / N))
print(lst[N // 2])

if len(lst2) != 1:
    if lst2[0][1] == lst2[1][1]:
        print(lst2[1][0])
    else:
        print(lst2[0][0])
else:
    print(lst2[0][0])

print(lst[-1] - lst[0])