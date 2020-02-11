# test = 'algorithm'
#
# test = test[::-1]
#
# print(test)
#
#
#
#


def atoi(st):
    value, digit = 0, 0
    for i in st:
        if i >= '0' and i <= '9':
            digit = ord(i) - ord('0')
        else:
            break
        value = (value*10) + digit
    return value
string = '3042'
print(atoi(string))


print(string[2])


for i in range(len(string), -1, -1):
    string[i] = ord(string[i] )
