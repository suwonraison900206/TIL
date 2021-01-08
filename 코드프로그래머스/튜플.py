def solution(s):
    answer = []

    q = ''

    print(s)

    for i in range(len(s)):
        if s[i] == '{':
            pass
        else:
            q = q + s[i]
    print(q)

    lst = q.split('}')
    print(lst)
    lst2 = []
    for i in range(len(lst)):
        if len(lst[i]) == 0:
            pass
        else:
            lst2.append(lst[i])
    for i in range(len(lst2)):
        if lst2[i][0] == ',':
            lst2[i] = lst[i][1:len(lst2[i])]

    print(lst2)

    lst2.sort(key=lambda x: len(x))
    lst3 = []
    print(lst2)
    print(type(lst2))

    lst3 = []
    lst4 = []

    for i in range(len(lst2)):
        lst3.append(lst2[i].split(','))


    print(lst3)

    for i in range(len(lst3)):
        for j in range(len(lst3[i])):
            if int(lst3[i][j]) not in lst4:
                lst4.append(int(lst3[i][j]))
    print(lst4)




# "{{2},{2,1},{2,1,3},{2,1,3,4}}"
s ="{{2},{2,1},{2,1,3},{2,1,3,4}}"

solution(s)