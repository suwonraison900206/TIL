def solution(gems):
    answer = []

    dict ={}

    for i in range(len(gems)):

        if gems[i] not in dict:
            dict[gems[i]] = [i+1]
        else:
            dict[gems[i]] += [i+1]
    print(dict)

    return answer

gems =["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
solution(gems)