from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    queue = deque(truck_weights)
    bridge_lst = [0] * bridge_length
    flag = 0
    while queue:
        flag_cnt = 0
        print(flag, queue, bridge_lst)
        if bridge_lst[-1] != 0:
            weight += bridge_lst[-1]
            bridge_lst[-1] = 0
            flag -= 1
            for i in range(len(bridge_lst) - 2, -1, -1):
                bridge_lst[i], bridge_lst[i + 1] = bridge_lst[i + 1], bridge_lst[i]
                flag_cnt +=1
                if flag -1 == flag_cnt:
                    break

            if weight >= queue[0]:
                target = queue.popleft()
                weight = weight - target
                bridge_lst[0] = target
                flag +=1

            answer += 1
        else:

            for i in range(len(bridge_lst)-2, -1, -1):

                bridge_lst[i], bridge_lst[i + 1] = bridge_lst[i + 1], bridge_lst[i]


            if weight >= queue[0]:
                target = queue.popleft()
                weight = weight - target
                bridge_lst[0] = target
                flag += 1

            answer += 1

    for j in range(len(bridge_lst)):
        if bridge_lst[j] != 0:
            print(len(bridge_lst) - j)
            return answer + len(bridge_lst) - j
    print(answer)

    return answer
bridge_length = 5
weight = 5
truck_weights = [2,2,2,2,1,1,1,1]

solution(bridge_length, weight, truck_weights)