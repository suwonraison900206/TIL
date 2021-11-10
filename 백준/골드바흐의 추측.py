T = int(input())
lst = [int(input()) for _ in range(T)]
number = [1] * (max(lst) + 1)
L = len(number)
prime_lst = []

for i in range(2, L):
    if number[i] == 1:
        prime_lst.append(i)
        for j in range(i*2, L, i):
            if number[j] == 1:
                number[j] = 0

for i in lst:
    target = []
    for j in range(len(prime_lst) // 2):
        if prime_lst[j] > i:
            break

        for k in range(j, len(prime_lst)):
            if j + k > i:
                break
            if prime_lst[j] + prime_lst[k] == i:
                target.append([prime_lst[j], prime_lst[k]])

    target.sort(key=lambda x: (x[1]-x[0]))

    print(target[0][0], target[0][1])

