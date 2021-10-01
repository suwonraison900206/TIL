while True:

    lst = list(input())
    result = []
    if len(lst) == 1 and lst[0] == '.':
        break
    big_flag = 0
    small_flag = 0
    for i in lst:

        if i == '[':
            result.append('[')
            big_flag +=1
        elif i == ']':
            if result:
                if result[-1] == '[':
                    result.pop()
                    big_flag-=1
                else:
                    print('no')
                    break
            else:
                print('no')
                break

        elif i == '(':
            small_flag +=1
            result.append('(')
        elif i == ')':
            if result:
                if result[-1] == '(':
                    result.pop()
                    small_flag -=1
                else:
                    print('no')
                    break
            else:
                print('no')
                break
    else:

        if big_flag == 0 and small_flag == 0:
            print('yes')
        else:
            print('no')