def solution(info, query):
    answer = []
    info_dict = {}
    for information in info:
        code, apply, year, food, score = information.split(' ')
        info_list = [code, apply, year, food]
        next_dict = info_dict
        for li in info_list:
            if li not in next_dict:
                next_dict[li] = {}
            next_dict = next_dict[li]

        print(info_dict)
    return answer


print(solution(	["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"], ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]))