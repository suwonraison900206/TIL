import heapq


def solution(k, room_number):
    answer = {}
    lst = []

    for number in room_number:
        if number not in answer:
            answer[number] = 1
        else:
            for i in range(number + 1, k):

                if i not in answer:
                    answer[i] = 1
                    break

    for key, value in answer.items():
        lst.append(key)

    return lst