def solution(key, lock):
    answer = True
    def turn_key(key):
        key_lst = []
        for i in range(len(key)):
            a = []

            for j in range(len(key)-1, -1, -1):
                a.append(key[j][i])
            key_lst.append(a)
        return key_lst

    lst = [[0] * (len(lock) * 3) for __ in range(len(lock) * 3)]

    for i in range(len(lock), (len(lock) * 2)):
        for j in range(len(lock), (len(lock) * 2)):
            lst[i][j] = lock[i-len(lock)][j - len(lock)]

    L = len(lst)
    K = len(key)
    for cnt in range(4):
        key = turn_key(key)
        for i in range(0, (L-K+1)):
            for j in range(0, (L-K+1)):
                flag = True

                for q in range(K):
                    for w in range(K):
                        lst[i+q][j+w] = lst[i+q][j+w] + key[q][w]

                for x in range(len(lock), (len(lock) * 2)):
                    for y in range(len(lock), (len(lock) * 2)):
                        if lst[x][y] == 0 or lst[x][y] == 2:
                            flag = False

                if flag == True:
                    return True

                for q in range(K):
                    for w in range(K):
                        lst[i+q][j+w] = lst[i+q][j+w] - key[q][w]

    return False


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

print(solution(key,lock))