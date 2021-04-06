def solution(food_times, k):
    answer = 0
    number = [i for i in range(len(food_times))]
    food_dict = {num: food_time for num, food_time in zip(number, food_times)}
    number.sort(key= lambda x:[x[0],x[1]])
    while food_dict:
        print(food_dict, k)
        min_value = min(food_dict.values())
        if k - (min_value * len(food_dict)) >= 0:
            k = k - (min_value * len(food_dict))
            food_dict = {key: (value - min_value) for key, value in food_dict.items() if value != min_value}

        else:
            count = k // len(food_dict)
            return k - (count*len(food_dict))

    return -1


food_times = [460, 560, 150, 600]
k = 1340

solution(food_times, k)