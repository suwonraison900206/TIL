import sys
sys.stdin = open("4880.txt")

# def cardbattle(a, b):
#     if a == 1:
#         if b == 2:
#             result.append(b)
#         else:
#             result.append(a)
#     if a == 2:
#         if b == 3:
#             result.append(b)
#         else:
#             result.append(a)
#     if a == 3:
#         if b == 1:
#             result.append(b)
#         else:
#             result.append(a)
# def cardgame(a, i , j):
#     k1 = a[i:(i+j)//2]
#     k2 = a[((i+j)//2):j]
#
#     if len(k1) > 2:
#         cardgame(k1, 0, len(k1))
#     elif len(k1) == 2:
#         cardbattle(k1[0], k1[1])
#     else:
#         return k1
#
#     if len(k2) > 2:
#         cardgame(k2, 0, len(k2))
#     elif len(k2) == 2:
#         cardbattle(k2[0], k2[1])
#     else:
#         return k2
#
#
# t = int(input())
#
# for test_case in range(t):
#     a = int(input())
#     k = list(map(int, input().split()))
#     result = []
#     cardgame(k, 0, len(k))
#
#     if len(result) == 1:
#         print(result)
#     else:
#         cardbattle(result[0], result[1])



def cardbattle(a, b):
    if a == 1:
        if b == 2:
            result.append(b)
        else:
            result.append(a)
    if a == 2:
        if b == 3:
            result.append(b)
        else:
            result.append(a)
    if a == 3:
        if b == 1:
            result.append(b)
        else:
            result.append(a)




def winner(x, y):
    if (n_list[y-1] == 1 and n_list[x-1] == 3) or (n_list[y-1] == 2 and n_list[x-1] == 1) or (n_list[y-1] == 3 and n_list[x-1] == 2):
        return y
    else:
        return x
def match(begin, finish):
    if begin == finish:
        return begin
    first_match = match(begin, (begin+finish)//2)
    second_match = match((begin+finish)//2+1, finish)
    return winner(first_match, second_match)
T = int(input())
for t in range(1, T+1):
    N = int(input())
    n_list = list(map(int, input().split()))
    start = 1
    end = N
    print('#{} {}'.format(t, match(start, end)))