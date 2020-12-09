def solution(bridge_length, weight, truck_weights):
    bridge_list = [0] * bridge_length

    print( bridge_length , weight, truck_weights)

    print(sum(bridge_list))
    count = 0
    while True:
        if count == 0:
            bridge_list[0] = truck_weights.pop(0)
            count += 1
            weight = weight - bridge_list[0]
        else:


            for i in range(len(bridge_list)-1,-1,-1):
                if i == len(bridge_list)-1:
                    weight = weight + bridge_list[i]
                    bridge_list[i] = 0
                else:
                    bridge_list[i+1] = bridge_list[i]
                    bridge_list[i] = 0
            if truck_weights:

                if weight - truck_weights[0] >=0:
                    bridge_list[0] = truck_weights.pop(0)
                    weight = weight - bridge_list[0]

            count = count + 1



        if sum(bridge_list) == 0:
            if len(truck_weights) == 0:
                print(count)
                return count


bridge_length = 100
weight = 100
truck_weights = [10]

solution(bridge_length, weight, truck_weights)