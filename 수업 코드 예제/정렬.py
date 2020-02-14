
a = int(input())


for i in range(((int(a/2)))):
    print(' ' * i,end='')
    print('*' * (a -(2 * i)),end='')
    print(' ' * i)
#
# for i in range(1):
#     print(' ' * (int(a/2)), end='')
#     print('*', end='')
#     print('' * (int(a/2)))
#

for i in range(((int(a/2))),-1,-1):
    print(' ' * i,end='')
    print('*' * (a -(2 * i)),end='')
    print(' ' * i)

