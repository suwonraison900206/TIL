def solution(n, times):
    answer = 0

    leng = len(times)
    left = 1
    right = (leng+1) * max(times)

    while left <= right:
        mid = (left + right) // 2

        count = 0
        for time in times:
            count += mid // time

            if count >= n: break

        if count >= n:
            answer = mid
            right = mid - 1

        elif count < n:
            left = mid + 1
    print(answer)
    return answer


n = 6
times =[7,10]
solution(n,times)