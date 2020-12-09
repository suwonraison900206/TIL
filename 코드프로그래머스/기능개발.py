def solution(progresses, speeds):
    answer = []
    release_list = []
    print(progresses, speeds)

    while progresses:
        if len(progresses) == 1:
            answer.append(1)
            break
        count = 0
        for i in range(len(progresses)):
            if progresses[i] + speeds[i] >= 100:
                progresses[i] = 100
            else:
                progresses[i] += speeds[i]

        if progresses[0] == 100:
            while True:
                if len(progresses) == 0:
                    answer.append(count)
                    break
                if progresses[0] == 100:
                    progresses.pop(0)
                    speeds.pop(0)
                    count += 1
                else:
                    answer.append(count)
                    count = 0
                    break

    return answer

progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]

solution(progresses, speeds)