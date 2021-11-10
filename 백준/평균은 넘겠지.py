C = int(input())

for test_case in range(1, C+1):
    lst = list(map(int,input().split()))
    N = lst[0]
    lst2 = lst[1:]
    average = sum(lst2) / N
    cnt = 0
    for i in lst2:
        if i > average:
            cnt +=1

    print(format((cnt / N) * 100, ".3f") + '%')
