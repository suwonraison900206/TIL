

S = list(map(int,input()))

check_list1 = 0
check_list2 = 0
check_number = 123


for num in S:

    if check_number == 1 or check_number == 0:
        pass
    else:
        if num == 0:
            check_number = num
            check_list1 = check_list1 + 1
        elif num == 1:
            check_number = num
            check_list2 = check_list2 + 1

    if num != check_number:
        if check_number == 0:
            check_list2 = check_list2 + 1
            check_number = 1
        else:
            check_list1 = check_list1 + 1
            check_number = 0




if check_list1 > check_list2:
    print(check_list2)
else:
    print(check_list1)


