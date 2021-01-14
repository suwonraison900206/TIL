def solution(gems):
    dict ={}

    for i in range(len(gems)):

        if gems[i] not in dict:
            dict[gems[i]] = 1

    missing = len(dict)

    stack2 = []
    left = start = end = 0
    for i in range(len(gems)):

        missing -= dict[gems[i]] > 0
        dict[gems[i]] -= 1

        if missing == 0:
            while left < i and dict[gems[left]] < 0:
                dict[gems[left]] += 1
                left +=1

            if not end or i - left <= end - start:
                stack2.append([i-left, left, i])
                start, end = left, i

                dict[gems[left]] +=1
                missing += 1
                left += 1

    stack2.sort(key=lambda x:(x[0], x[1]))
    a = stack2[0]
    answer = [a[1] +1, a[2]]
    print(answer)
    return answer

gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
solution(gems)