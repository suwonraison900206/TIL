T = int(input())

for _ in range(T):

    a = list(input())
    lst = []
    left = 0

    for i in a:
        if i == '(':
            lst.append('(')
            left +=1
        elif i == ')':

            if left == 0:

                print('NO')
                break
            else:
                left -=1
                if lst[-1] != '(':
                    print('NO')
                    break
                else:
                    lst.pop()
    else:
        if left == 0:
            print('YES')
        else:
            print('NO')
