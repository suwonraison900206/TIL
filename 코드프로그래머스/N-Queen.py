from itertools import combinations, permutations

def solution(n):
    answer = 0
    chess = [[0] * n for __ in range(n)]

    queen_list = []

    q = permutations(k,4)

    print(list(q))


    return answer


n = 4
solution(n)