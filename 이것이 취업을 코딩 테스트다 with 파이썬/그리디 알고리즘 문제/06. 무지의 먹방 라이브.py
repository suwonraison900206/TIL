def solution(food_times, k):
    answer = 0

    if sum(food_times) <= k:
        answer = -1
        return answer




    min_value = min(food_times)

    if (min_value * len(food_times)) < k:
        for i in range(len(food_times)):
            food_times[i] = food_times[i] - min_value
            k = k - min_value

    while k != -1:
        for i in range(len(food_times)):
            if food_times[i] != 0:
                food_times[i] = food_times[i] - 1
                k = k - 1
            if k == -1:
                answer = i + 1
                return answer


food_times = [460, 560, 40, 600]
k = 1340


print(solution(food_times, k))