from itertools import permutations




def solution(n, weak, dist):
    weak_n = len(weak)
    dist_n = len(dist)
    for i in range(weak_n): # 반시계 방향을 선형으로 만들기
        weak.append(weak[i] + n)

    for i in range(0, weak_n+1):

        check_weak = weak[i:i + weak_n]

        for j in range(n):

            for q in permutations(dist):

                print(q, check_weak)




    return
n = 12
weak = [1, 5, 6, 10]
dist = 	[1, 2, 3, 4]
solution(n, weak, dist)
