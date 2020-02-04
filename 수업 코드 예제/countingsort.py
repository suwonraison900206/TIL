def Counting_Sort(inp, out, k):
    # A [1 .. n] -- 입력 배열(1 to k)
    # B [1 .. n] -- 정렬된 배열.
    # C [1 .. k] -- 카운트 배열.

    cnt = [0] * k

    for i in range (0, len(out)):
        cnt[inp[i]] += 1

    for i in range (1, len(cnt)):
        cnt[i] += cnt[i-1]

    for i in range (len(out)-1, -1, -1):
        out[cnt[inp[i]]- 1] = inp[i]
        cnt[inp[i]] -= 1
    return out

a = [0, 4, 1, 3, 1, 2, 4, 1]
b = [0]*len(a)
c = max(a) + 1


print(Counting_Sort(a,b,c))

