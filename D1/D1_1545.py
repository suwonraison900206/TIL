a = int(input())

b = []

for i in range(a+1):
    b.append(i)


c = b[::-1]
print(' '.join(map(str, c)))