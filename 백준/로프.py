n = int(input())
lst = [int(input()) for _ in range(n)]
lst.sort(reverse=True)
cnt = 0
target = 0
max_result = 0
for i in lst:

    cnt += 1
    target += i
    result = target // cnt

    if cnt > 1:
        if result > i:
            result = i

    final_result = result * cnt
    if final_result > max_result:
        max_result = final_result

print(max_result)
