def backtrack(a, k, N, s):
    if s > 10: return      # 가지치기
    # 현재까지 만들어진 부분집합의 원소들의 합이 10보다 크면 종료

    if k == N:         # N번째 단계까지 왔을 때
        if s == 10:    # 부분집합의 합이 0 일 경우
            for i in range(N):     # a[]에 부분집합이 될 원소의 포함여부에 따라서 부분집합의 원소 출력
                if a[i]: print(S[i], end=' ')
            print()
    else:
        a[k] = 0                         # k 번째 원소 선택 안하는 경우
        backtrack(a, k + 1, N, s)    # k  번째 원소를 선택하지 않았으므로 s 에 해당원소 더하지 않고 다음 단계 호출
        if s+S[k] <= 10:               # k 번째 원소를 더한 합이 10 보다 작거나 같을 경우에만 (가지 치기)
            a[k] = 1                     # k 번째 원소 선택
            backtrack(a, k + 1, N, s + S[k])    # k 번째 원소를 선택했으므로 s 에 k 번째 원소를 더하고 다음 단계 호출



a = [0] * 10
S = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
backtrack(a, 0, 10, 0)





#
# a =[0] * 4
# def backtrack(a, k, input):
#     #print(a,k)
#     if k == input:
#         print(a)
#     else:
#         k += 1
#         a[k] = 1
#         backtrack(a, k, input)
#         a[k] = 0
#         backtrack(a, k, input)
# backtrack(a, 0, 3)




