def solution(n, computers):
    def DFS(target, computers, check_list, answer, n):
        for i in range(n):

            if computers[target][i] == 1 and check_list[i] == 0:
                check_list[i] = answer
                DFS(i, computers, check_list, answer, n)




    answer = 1
    check_list = [0] * n
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and check_list[j] == 0:
                check_list[j] = answer
                DFS(j, computers, check_list, answer, n)
                answer +=1

    
    return answer


n = 3
computers =	[[1, 1, 0], [1, 1, 0], [0, 0, 1]]
solution(n, computers)