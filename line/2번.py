def solution(answer_sheet, sheets):

    answer_sheet_lst = []
    stack = []

    for i in range(len(answer_sheet)):
        answer_sheet_lst.append(answer_sheet[i])
    sheets_lst =[]
    sheets_lst2 = []


    for i in range(len(sheets)):
        for j in range(len(answer_sheet)):
            sheets_lst.append(sheets[i][j])
        sheets_lst2.append(sheets_lst)
        sheets_lst=[]

    for i in range(len(sheets_lst2)):
        for j in range(len(answer_sheet)):
            if answer_sheet[j] == sheets_lst2[i][j]:
                sheets_lst2[i][j] = 0


    result = []
    while len(sheets_lst2) !=1:
        k = len(sheets_lst2)
        if k > 1:
            for i in range(1,k):
                cnt = 0
                trailng_cnt = 1
                trailng_cnt2 = 0
                for j in range(len(answer_sheet_lst)):
                    if sheets_lst2[0][j] == sheets_lst2[i][j] and sheets_lst2[0][j] != 0:
                        cnt = cnt +1
                        if j+1 < len(answer_sheet_lst) and sheets_lst2[0][j+1] == sheets_lst2[i][j+1] and sheets_lst2[i][j+1] != 0:
                            trailng_cnt += 1
                    else:
                        trailng_cnt2 = trailng_cnt
                        trailng_cnt = 1

                stack.append([cnt, trailng_cnt2])
            sheets_lst2.pop(0)

    k_lst = []

    for i in range(len(stack)):
        k = stack[i][0] + (stack[i][1] * stack[i][1])
        k_lst.append(k)

    if max(k_lst) == 1:
        print(0)
        return 0
    else:
        print(max(k_lst))
        return max(k_lst)


answer_sheet = "53241"
sheets =["53241", "42133", "53241", "14354"]

solution(answer_sheet,sheets)