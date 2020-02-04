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


T = int(input())

for test_case in range(T):
    temp = list(map(int, input().split()))


    start = 1
    end = temp[0]
    while start <= end:
        middle = (start + end) // 2
        if middle == temp[1]:
            print('a')
        elif middle > temp[1]:
            middle = (middle + temp[0]) // 2
        else:


