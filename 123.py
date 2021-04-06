def solution(n):

    i, j  = 1,1

    for q in range(n):

        i, j = j , i+j
        print(i,j)

    print(i, j )




n = 5
print(solution(n))