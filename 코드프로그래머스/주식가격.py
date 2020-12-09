def solution(prices):
    answer = [0] * len(prices)

    for i in range(len(prices)-1):
        count = 0
        cnt = prices[i]

        for j in range(i+1, len(prices)):
            count += 1
            if cnt <= prices[j]:
                pass
            else:
                answer[i] = count
                break
        answer[i] = count

    return answer


prices = [1, 2, 3, 2, 3]

solution(prices)