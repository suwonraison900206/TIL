x,y,w,h = map(int,input().split())

print(x,y,w,h)
cnt = 0
row = [0, w]
column = [0, h]

print(x,y)
result = []
for i in row:
    result.append(abs(i-x))

for i in column:
    result.append(abs(i-y))

print(min(result))