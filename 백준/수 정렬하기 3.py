N = int(input())
lst = list(map(int,input().split()))
lst2 = list(sorted(set(lst)))

number_dict = {}
for i in range(len(lst2)):
    number_dict[lst2[i]] = i


for i in lst:
    print(number_dict[i], end=' ')