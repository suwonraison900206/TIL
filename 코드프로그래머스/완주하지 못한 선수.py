def solution(participant, completion):


    compare_a = {}
    compare_b = {}

    for i in participant:
        if i in compare_a:
            compare_a[i] += 1
        else:
            compare_a[i] = 1



    for i in completion:
        if i in compare_b:
            compare_b[i] += 1
        else:
            compare_b[i] = 1



    for i in compare_b:
        if i in compare_a:
            compare_a[i] -= compare_b[i]

    for i in compare_a:

        if compare_a[i] == 1:
            answer = i
            break
    return answer


participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
solution(participant,completion)