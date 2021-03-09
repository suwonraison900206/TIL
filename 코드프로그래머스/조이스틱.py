def solution(name):
    answer = 0
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    number = [i for i in range(len(alphabet))]
    dict = {i: min(j, abs(j - len(alphabet))) for i, j in zip(alphabet, number)}
    print(dict)
    name_list = []
    for i in range(len(name)):
        name_list.append(name[i:len(name)] + name[0:i])
    q = set(name_list)
    result_lst = []

    for i in range(len(name_list)):
        init_name = 'A' * len(name)
        cnt = 0
        word = ''
        for j in range(len(name_list[i])):
            print(name_list[i][j])
            if init_name[j] != name_list[i][j]:
                cnt = cnt + dict[name_list[i][j]]
                word += name_list[i][j]
                if word + ('A' * (len(name_list[i]) - len(word))) in q:
                    result_lst.append(cnt)

            else:
                word += name_list[i][j]
                if word + ('A' * (len(name_list[i]) - len(word))) in q:
                    result_lst.append(cnt)

            cnt = cnt + 1
    print(result_lst)
    return min(result_lst)


name = "AZAAAZ"

solution(name)
