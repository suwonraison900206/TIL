def solution(stones, k):
    answer = 0

    while (answer != k):
        answer = 0
        for i in range(len(stones)):
            if stones[i] != 0:
                cnt = 0
                stones[i] = stones[i] - 1
            else:
                answer = answer + 1
                if answer == k:
                    break
    return answer

stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3

solution(stones,k)