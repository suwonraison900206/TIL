d= ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

a = 10

b = 3

c = []


e = []
result = 0
f = 0
result1 = []
for i in range(a - b +1):
    c.append(d[i:b+i])

for j in range(0, len(c)):
    result1.append(result)
    result = 0
    for z in range(0, b):
        result = result + int(c[j][z])
result1.append(result)

print(max(result1) - (result1[1]))


#
# print(len(c))
#
# for j in range(0, len(c)):
#     print((c[j]))