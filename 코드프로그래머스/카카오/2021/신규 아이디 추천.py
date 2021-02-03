def solution(new_id):
    check_list = "qwertyuiopasdfghjklzxcvbnm1234567890-_."
    new_id = new_id.lower()

    step_2 = ''
    for i in new_id:
        if i in check_list:
            step_2 = step_2 + i

    step_3 = ''

    for i in range(len(step_2)):
        if i == 0:
            step_3 = step_3 + step_2[i]
        else:
            if step_2[i] == '.' and step_2[i-1] == '.':
                pass
            else:
                step_3 = step_3 + step_2[i]

    print(step_3)


    if len(step_3) != 0:
        if step_3[0] == '.':
            step_3 = step_3[1:len(step_3)]

        if len(step_3) !=0 and step_3[-1] == '.':
            step_3 = step_3[0:len(step_3)-1]

    print(step_3)


    if len(step_3) == 0:
        step_3 = step_3 + 'a'
    if len(step_3) >= 16:
        step_3 = step_3[0:15]
    elif len(step_3) <= 2:
        step_3 = step_3 + (step_3[-1] * (3 - len(step_3)))

    if len(step_3) != 0:
        if step_3[0] == '.':
            step_3 = step_3[1:len(step_3)]

        if len(step_3) !=0 and step_3[-1] == '.':
            step_3 = step_3[0:len(step_3)-1]


    print(step_3)

    return step_3



new_id ="abcdefghijklmn.p"
solution(new_id)