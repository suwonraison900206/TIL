def solution(road, n):
    road_lst = []
    zero_count = 0

    result = []
    stack = []

    for i in range(len(road)):
        road_lst.append(int(road[i]))
    while True:
        road_lst2 = road_lst[:]
        for i in range(len(road_lst2)):
            if road_lst2[i] == 0 and zero_count < n:
                road_lst2[i] = 1
                stack.append(i)
                zero_count = zero_count + 1
            elif road_lst2[i] == 0 and zero_count == n:
                result.append(i)
                road_lst = road_lst[stack[0]+1:]
                zero_count = 0
                stack = []
                break

        if zero_count != 0:
            stack.append(i)
            result.append(i+1)
            print(max(result))
            print(result)

            return max(result)


road = "111011110011111011111100011111"

n = 3

solution(road,n)