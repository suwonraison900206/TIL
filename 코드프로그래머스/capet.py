def solution(brown, yellow):
    answer = []

    count = brown + yellow
    # 가로길이는 세로 길이와 같거나, 세로 길이보다 깁니다.
    list =[]

    for i in range(1, count+1):
        if (count) % i == 0:
            if i >= count // i:
                list.append([i, count //i])

    for i in range(len(list)):
        map_lst = [[0] * list[i][0] for __ in range(list[i][1])]
        count = 0
        for j in range(1, len(map_lst[0])-1):
            for k in range(1, len(map_lst)-1):
                count = count + 1
        if count == yellow:
            return list[i]



    return answer

brown = 8
yellow = 1

solution(brown,yellow)