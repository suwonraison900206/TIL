def solution(name):
    answer = 0

    DICT_list ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    count_list = []

    name_list = []
    for i in range(len(name)-1):
        name_list.append(name[i:len(name)] + name[0:i])
    print(name_list)
    for i in range(len(name_list)):
        answer = 0
        sample = ['A'] * len(name)
        for q in range(len(name_list[i])):
            if q == 0:
                count = 0
            else:
                answer = answer + 1
                count = 0
            for j in range(len(DICT_list)):
                if DICT_list[j] == name_list[i][q]:
                    sample[q] = DICT_list[j]
                    break
                count = count + 1

            if count > len(DICT_list) - count:
                answer = answer +  (len(DICT_list) - count)
            else:
                answer = answer + count
            if "".join(sample) == name_list[i]:
                break
        count_list.append(answer)
    print(count_list)
    print(min(count_list))

    return min(count_list)


name ='ABAAAAABAB'

solution(name)
