import sys
sys.stdin = open("retire.txt")

N = int(input())

lst = []

for i in range(N):
    lst.append(list(map(int,input().split())))

for i in range(N):
    if i + lst[i][0] > N:
        lst[i][0] = 0
        lst[i][1] = 0

print(lst)

count = 0
day = 0
result = []
lst2 =[]
final_result = 0

for j in range(len(lst)-1, -1, -1):
    count = count + 1
    if lst[j][0] == 1 or lst[j][0] == 0:
        result.append(lst[j][1])
        final_result = final_result + lst[j][1]
    else:
        result.append(lst[j][1])
        lst2 = result[::-1]
        lst2 = lst2[0:lst[j][0]]
        print(sum(lst2))
        if lst[j][1] >= sum(lst2):
            final_result = final_result + lst[j][1]
            lst2=[]
        else:
            result.pop(-1)
            result.append(0)
print(final_result)

