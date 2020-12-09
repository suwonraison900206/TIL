def solution(priorities, location):
    answer = 0
    count = 0

    priorities_locate = [0] * len(priorities)

    for i in range(len(priorities_locate)):
        priorities_locate[i] = count
        count +=1
    cnt = 0
    while True:
        k = priorities.pop(0)
        k_locate = priorities_locate.pop(0)

        if priorities:

            if k >= max(priorities):
                if k_locate == location:
                    cnt += 1
                    return cnt
                cnt += 1
            else:
                priorities.append(k)
                priorities_locate.append(k_locate)
        else:
            cnt +=1
            return cnt




    return answer

priorities = [2, 1, 3, 2]
location = 2

solution(priorities, location)