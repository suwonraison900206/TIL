def solution(citations):
    answer = 0

    print(citations)

    citations.sort(reverse=True)
    print(citations)
    count = citations[0] +1
    for i in range(len(citations)):

        count -=1
        cnt = 0

        for j in range(len(citations)):
            if citations[j] >= count:
                cnt += 1

        if cnt >= count:
            print(cnt)
            return cnt

    return answer


citations = [3, 0, 6, 1, 5]
solution(citations)