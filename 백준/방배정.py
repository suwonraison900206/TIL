def solution(k, room_number):
    answer = []
    visit_lst = [0] * (k+1)
    reservation = []
    for i in range(len(room_number)):
        if visit_lst[room_number[i]] == 0:
            visit_lst[room_number[i]] = 1
            answer.append(room_number[i])
        else:
            reservation.append(room_number[i])

    for i in range(len(reservation)):
        if visit_lst[room_number[i]] != 0:
            for j in range(1, len(visit_lst)):
                if visit_lst[j] == 0:
                    visit_lst[j] = 1
                    answer.append(j)
                    break




    return answer

k = 10
room_number = [1,3,4,1,3,1]

solution(k, room_number)