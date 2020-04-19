

T = int(input())

for test_case in range(T):

    inp = str(input())
    s = []
    for i in range(0, len(inp)-2, 3):
        s.append(inp[i:i+3])
    space = 13
    dia = 13
    clover = 13
    hart = 13
    space_2 =[]
    dia_2 = []
    clover_2 = []
    hart_2 = []
    cnt = 0

    for i in range(len(s)):
        if s[i][0] == 'S':
            if s[i] in space_2:
                cnt = cnt + 1
            else:
                space_2.append(s[i])
        elif s[i][0] == 'D':
            if s[i] in dia_2:
                cnt = cnt + 1
            else:
                dia_2.append(s[i])
        elif s[i][0] == 'C':
            if s[i] in clover_2:
                cnt = cnt + 1
            else:
                clover_2.append(s[i])
        elif s[i][0] == 'H':
            if s[i] in hart_2:
                cnt = cnt + 1
            else:
                hart_2.append(s[i])
    print(space_2)
    print(dia_2)
    print(clover_2)
    print(hart_2)
    if cnt != 0:
        print('#{} ERROR'.format(test_case + 1))
    else:
        print('#{} {} {} {} {}'.format(test_case + 1, space - len(space_2), dia - len(dia_2), hart - len(hart_2), clover - len(clover_2)))