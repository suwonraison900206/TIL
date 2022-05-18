H, W = map(int, input().split())
lst = list(map(int, input().split()))

print(H, W)
print(lst)
L = len(lst)
start, end = 0, 0
count = 0
while True:

    if lst[start] == 0:

        start += 1
    else:
        end = start +2
        if end > L:
            break
        while True:

            if lst[end] != 0:

                w = min(lst[start], lst[end])

                for i in range(start+1, end+1):
                    print(i)






