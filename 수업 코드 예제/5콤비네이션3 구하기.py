def backtrack(a, k, N):
    if k == N:
        if sum(a) == 3:
            list_k.append(a[:])
            print(a)
    else:
        a[k] = 0
        backtrack(a, k+1, N)
        a[k] = 1
        backtrack(a, k+1, N)


a = [0] * 5
list_k = []
backtrack(a, 0, 5)

print(list_k)


