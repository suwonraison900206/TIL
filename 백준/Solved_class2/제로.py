K = int(input())

lst = []

for i in range(K):
    a = int(input())
    if a != 0:
        lst.append(a)
    else:
        lst.pop()

if not lst:
    print(0)
else:
    print(sum(lst))