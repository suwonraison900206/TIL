
def solution(key, lock):
    answer = False
    n = len(lock)
    new_lock = [[0] * (n * 3) for __ in range(n * 3)]
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]

    count = 0

    result = 0
    for i in range(len(lock)):
        result = result + sum(lock[i])

    cnt = 0
    for turn in range(4):
        key = turn_right(key)
        for k in range(len(new_lock) - len(key) +1):
            for r in range(len(new_lock) - len(key) +1):

                for q in range(len(key)):
                    for w in range(len(key)):
                        new_lock[k+q][r+w] = new_lock[k+q][r+w] + key[q][w]

                for a in range(len(lock)):
                    for b in range(len(lock)):
                        if new_lock[len(lock) + a][len(lock) + b] == 1:
                            count = count + 1

                if count == (len(lock) * len(lock)):
                    answer = True
                    return answer
                for q in range(len(key)):
                    for w in range(len(key)):
                        new_lock[k + q][r + w] = new_lock[k + q][r + w] - key[q][w]
                count = 0

    return answer

def turn_right(turn_key):
    b = [[] for _ in range(len(turn_key))]

    for i in range(len(turn_key)):
        b[i] = [turn_key[j][i] for j in range(len(turn_key)-1, -1, -1)]

    return b

key =[[0, 0, 0], [1, 0, 0], [0, 1, 1]]

lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

print(solution(key,lock))