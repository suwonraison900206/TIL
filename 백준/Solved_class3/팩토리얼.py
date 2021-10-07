import math
N = int(input())

a = str(math.factorial(N))

cnt = 0
for i in range(len(a)-1,-1,-1):

    if a[i] == '0':
        cnt +=1
    else:
        break
print(cnt)