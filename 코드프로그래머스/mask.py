# def solution(clothes):
#     def backtracking(idx, wear, cnt):
#         for i in range(idx + 1, len(clothes)):
#             if clothes[i][1] not in wear:
#                 cnt.append(1)
#                 wear.append(clothes[i][1])
#                 backtracking(i, wear, cnt)
#                 wear.pop()
#
#     clothes.sort(key=lambda x: x[1])
#     cnt = []
#     for i in range(len(clothes)):
#         cnt.append(1)
#         backtracking(i, [clothes[i][1]], cnt)
#
#     return cnt.count(1)


# def solution(clothes):
#     lst = [0, 0, 0, 0]
#
#     for i in range(len(clothes)):
#         if clothes[i][1] == 'headgear':
#             lst[0] += 1
#         elif clothes[i][1] == 'eyewear':
#             lst[1] += 1
#         elif clothes[i][1] == 'face':
#             lst[2] += 1
#         else:
#             lst[3] += 1
#
#     cnt = 1
#     for i in range(len(lst)):
#         if lst[i] != 0:
#             cnt = cnt * (lst[i] + 1)
#
#     cnt = cnt - 1
#     print(lst)
#     print(cnt)
#     return cnt
#
# clothes = 	[["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
# solution(clothes)


def solution(clothes):
    A = {}
    for i in clothes:
        if i[1] not in A:
            A[i[1]] = 1
        else:
            A[i[1]] += 1
    print(A)
    N1, N2 = 0, 1

    for i in A.values():
        N2 *= i + 1
    return N2 - 1


clothes = 	[["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
solution(clothes)