from itertools import combinations ,permutations

def solution(info, query):
    answer = []
    # print(info)
    # print(query)
    query_lst = []
    for i in range(len(query)):
        query_lst.append(list(map(str,query[i].split('and'))))

    # print(query_lst)
    # print(len(query_lst))

    # q = {}
    #
    info_lst = []
    for i in range(len(info)):
        info_lst.append(list(map(str,info[i].split(' '))))
    print(info_lst)
    print(query_lst)
    for i in range(len(query_lst)):
        cnt = 0
        for j in range(len(info_lst)):
            for q in range(5):
                if query_lst[i]


    # print(info_lst)
    #
    # for i in range(len(info_lst)):
    #     pass
    return answer


info =["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

solution(info,query)