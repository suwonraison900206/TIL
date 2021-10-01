T = int(input())

lst = []

for i in range(T):

    age, name = input().split()
    lst.append([int(age),name,i])
lst.sort(key=lambda x:(x[0],x[2]))

for age, name, number in lst:
    print(age, name)

