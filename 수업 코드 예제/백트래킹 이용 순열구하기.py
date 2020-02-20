def backtrack(a, k, N):
    c = [0] * N
    if k == N:
        print(a)
    else:
        in_perm = [False] * N
        for i in range(k):
            in_perm[a[i]] = True
        ncandidates = 0
        for i in range(N):
            if in_perm[i] == False:
                c[ncandidates] = i
                ncandidates += 1
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k+1, N)
a = [0] * 4
backtrack(a, 0, 4)


#
#
#
# def construct_candidates(a, k, N, c):
#     in_perm = [False] * N
#
#     for i in range(1, k):
#         in_perm[a[i]] = True
#
#     ncandidates = 0
#     for i in range(1, N + 1):
#         if in_perm[i] == False