from itertools import combinations


def solution(info, query):
    answer = []
    survey_dict = {}

    def devide(INFO):
        survey_lst = []
        number = [0, 1, 2, 3]

        for n in range(0, 5):
            for j in combinations(number, n):
                copy_INFO = INFO[:]
                for q in j:
                    copy_INFO[q] = '-'
                survey_lst.append(''.join(copy_INFO))
        return survey_lst

    for i in info:
        information = i.split()
        survey_info = information[:4]
        score = int(information[-1])
        w = devide(survey_info)
        for ii in w:
            if ii not in survey_dict:
                survey_dict[ii] = [score]
            else:
                survey_dict[ii].append(score)

    for key, value in survey_dict.items():
        survey_dict[key].sort()
    print(len(survey_dict))
    for i in query:
        qu = i.split()
        qu_info = qu[:7]
        qu_score = int(qu[-1])
        sample = ''
        for ii in range(0, len(qu_info), 2):
            sample += qu_info[ii]

        if sample not in survey_dict:
            answer.append(0)

        else:

            start = 0
            end = len(survey_dict[sample])

            while start < end:
                mid = (start + end) // 2
                if survey_dict[sample][mid] >= qu_score:
                    end = mid
                else:
                    start = mid + 1

            answer.append(len(survey_dict[sample]) - start)
    print(answer)
    return answer


info = ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
        "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
         "- and - and - and - 150"]

solution(info, query)