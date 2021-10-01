N = int(input())

students = [list(map(int,input().split())) for __ in range(N)]
result = []
for i, student in enumerate(students):
    cnt = 1

    for j, studnet2 in enumerate(students):


        if student[0] < studnet2[0] and student[1] < studnet2[1]:
            cnt +=1

    print(cnt, end=' ')
