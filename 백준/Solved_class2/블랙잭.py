def backtrack(lst, idx, cnt, result, M):
    global result_lst
    if cnt == 3:
        if result > M:
            return
        result_lst.append([abs(M-result),result])
        return

    for i in range(idx+1, len(lst)):

        backtrack(lst, i, cnt+1, result + lst[i], M)




N, M = map(int,input().split())
lst = list(map(int,input().split()))
result_lst = []

backtrack(lst,0, 0, 0, M)
result_lst.sort(key=lambda x: x[0])
print(result_lst[0][1])
