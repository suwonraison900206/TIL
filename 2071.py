# a = (22, 8, 5, 123, 7, 2, 63, 7, 3, 46)
# b = 0
# c = 0
# d = 0
# e = 0
# f = 0
# str(a)
# for i in a:
#     b = int(i)
#     c = c + b
#     e = e + 1
# f = c / e


a = int(input())
k = []
b = 0
cout = 0
c = 0
for i in range(a):
    b = b + i  
    cout = cout + 1    
c = b / cout
k.append(c)
for i in range(0, a):
    print('#{} {}'.format(i+1, k[i]))