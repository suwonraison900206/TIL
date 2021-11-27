def back(target, number, cnt):
    global k
    if sum(cnt) == target:
        k += 1

        return
    elif sum(cnt) > target:
        return

    for i in number:

        back(target, number, cnt + [i])




T = int(input())
lst = [int(input()) for _ in range(T)]
number = [1,2,3]
for n in lst:
    k = 0
    back(n, number, [])

    print(k)






