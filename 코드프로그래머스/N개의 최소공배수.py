def solution(arr):
    answer = 0
    arr.sort(reverse=True)
    stack = []
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i - 1, -1, -1):

            if arr[j] % arr[i] == 0:
                arr[j] = arr[j] // arr[i]
            else:
                pass
        stack.append(arr[i])
    stack.append(arr[0])

    cnt = 1
    for i in range(len(stack)):
        cnt = cnt * stack[i]
    print(cnt)
    return cnt

arr = [360, 17]
solution(arr)