# def binarysearch(a, key):
#     start = 0
#     end = len(a) - 1
#     while start <= end :
#         middle = (start + end) //2
#         if a[middle] == key:
#             return True
#         elif a[middle] > key :
#             end = middle -1
#         else :
#             start = middle + 1
#     return False
#
# a = [2, 4, 7, 9, 11, 19, 23]
#
# print(binarysearch(a, 23))

#
# T = int(input())
#
# for test_case in range(T):
#     temp = list(map(int, input().split()))
#     start = 1
#     end = temp[0]
#     cnt = 0
#     cnt2 = 0
#     middle = (start + end) // 2
#     middle2 = (start + end) // 2
#     i = 0
#     j = 0
#     while i == 0:
#
#         if middle == temp[1]:
#              i = 1
#         elif middle > temp[1]:
#             middle = middle - (temp[0] * ((0.5) ** (cnt2 + 2)))
#             cnt = cnt + 1
#         else:  # middle < temp[1]:
#             middle = middle + (temp[0] * ((0.5) ** (cnt2 + 2)))
#             cnt = cnt + 1
#     while j == 0:
#
#         if middle2 == temp[2]:
#             j = 1
#         elif middle2 > temp[2]:
#             middle2 = (middle2 - (temp[0] * ((0.5) ** (cnt2 + 2)))) // 1
#             cnt2 = cnt2 + 1
#
#         else:  # middle < temp[1]:
#             middle2 = (middle2 + (temp[0] * ((0.5) ** (cnt2 + 2)))) // 1
#             cnt2 = cnt2 + 1
#
#
#     if cnt == cnt2:
#         print('#{} "O" '.format(test_case + 1))
#     elif cnt > cnt2:
#         print('#{} "A" '.format(test_case + 1))
#     else:
#         print('#{} "B" '.format(test_case + 1))

    # def binarysearch(a, key):
    #     start = 0
    #     end = len(a) - 1
    #     while start <= end :
    #         middle = (start + end) //2
    #         if a[middle] == key:
    #             return True
    #         elif a[middle] > key :
    #             end = middle -1
    #         else :
    #             start = middle + 1
    #     return False
    #
    # a = [2, 4, 7, 9, 11, 19, 23]
    #
    # print(binarysearch(a, 23))






# [파이썬 S/W 문제해결 기본] 2일차 - 이진검색
def binarySearch(end,key):
    start = 1
    cnt = 0
    while abs(start-end) != 1:
        middle = int((start + end) / 2)
        if middle == key:
            cnt += 1
            return cnt # 검색 성공
        elif middle > key:
            cnt += 1
            end = middle
        else:
            start = middle
            cnt += 1
    return False # 검색 실패
T = int(input())
for i in range(T):
    temp = list(map(int,input().split()))
    far= temp[0]
    pa = temp[1]
    pb = temp[2]
    cnt1 = binarySearch(far,pa)
    cnt2= binarySearch(far,pb)
    result = ''
    if cnt1 > cnt2:
        result = 'B'
    elif cnt1 == cnt2:
        result = 0
    else:
        result = 'A'
    print("#{0} {1}".format(i+1,result))





