def solution(numbers):
    answer = []

    for number in numbers:
        b = format(number, 'b')
        lst = []
        print(b)
        for i in b:

            for j in i:

                lst.append(j)
        flag = 0
        for i in range(len(lst)-1,-1,-1):
            print(i)
            if int(lst[i]) == 0:
                if flag == 1:
                    lst[i+1] = '0'
                    lst[i] = '1'
                    break
                elif flag == 0:
                    lst[i] = '1'
                    break
            else:
                flag = 1
                if i == 0 and flag == 1:
                    lst[0] = '10'

        s = ''.join(lst)
        s = s[::-1]
        ten = 0

        for i in range(len(s)):
            if i == 0:
                x = 1 if s[int(i)] == '1' else 0
                ten += x

            else:
                if s[i] == '1':
                    ten = ten + (2 ** i)
        print(ten)

        answer.append(ten)





    return answer





numbers = [3, 7]
solution(numbers)