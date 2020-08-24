def solution(food_times, k):
    answer = 0

    if sum(food_times) <= k:
        answer = -1
        return answer

    length = len(food_times)
    min_value_lst = []
    count = 0
    food_times.sort()
    for i in range(len(food_times)):
        if i == 0:
            min_value_lst.append(sum(food_times[0:i+1]))
        else:
            min_value_lst.append(food_times[i] - food_times[i-1])
    print(123)
    for i in range(len(min_value_lst)):
        count = min_value_lst[i]
        print(count)
        if (count * length) < k:
            for j in range(len(food_times)):
                food_times[j] = food_times[j] - count
                k = k - count
                if k == 0:
                    print(123)
                    break
        else:
            for j in range(len(food_times)):
                food_times[j] = food_times[j] - 1
                k = k - 1
                if k == 0:
                    print(123)
                    break


food_times = [460, 560, 40, 600]
k = 1340


solution(food_times, k)