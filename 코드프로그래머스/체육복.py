def solution(n, lost, reserve):

    students_lst = [1] * n
    print(lost, reserve)
    print(students_lst)

    for i in range(len(lost)):
        students_lst[lost[i]-1] = 0

    for i in range(len(reserve)):
        students_lst[reserve[i] -1] += 1

    for i in range(len(students_lst)):
        if students_lst[i] ==0:
            if i == 0:
                if students_lst[i+1] > 1:
                    students_lst[i + 1] -= 1
                    students_lst[i] = 1

            elif i == len(students_lst) -1:
                if students_lst[i-1] > 1:
                    students_lst[i-1] -=1
                    students_lst[i] = 1
            else:
                if students_lst[i-1] > 1:
                    students_lst[i-1] -=1
                    students_lst[i] = 1
                elif students_lst[i+1] > 1:
                    students_lst[i+1] -=1
                    students_lst[i] = 1

    print(students_lst)
    answer = 0
    for i in range(len(students_lst)):
        if students_lst[i] != 0:
            answer +=1

    return answer


n = 5
lost = [2,4]
reserve =[1,3,5]

solution(n,lost,reserve)