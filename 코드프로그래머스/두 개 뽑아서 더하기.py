def solution(numbers):
    answer = []

    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            answer.append(numbers[i] + numbers[j])
    answer2 = sorted(list(set(answer)))
    print(answer2)

    return answer2


numbers = [5,0,2,7]
solution(numbers)