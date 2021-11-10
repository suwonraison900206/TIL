# def merge_sort(unsorted_lst):
#
#     if len(unsorted_lst) <= 1:
#         return unsorted_lst
#
#     mid = len(unsorted_lst) // 2
#     left = merge_sort(unsorted_lst[:mid])
#     right = merge_sort(unsorted_lst[mid:])
#
#     return merge(left, right)
#
#
# def merge(left, right):
#     i, j = 0, 0
#     sort_lst = []
#     while(i<len(left) and j<len(right)):
#
#         if left[i] <= right[j]:
#             sort_lst.append(left[i])
#             i += 1
#         else:
#             sort_lst.append(right[j])
#             j += 1
#
#         if i == len(left):
#             sort_lst += right[j:len(right)]
#
#         if j == len(right):
#             sort_lst += left[i:len(left)]
#
#     return sort_lst
def quick(unsort):
    if len(unsort) <= 1:
        return unsort

    pivot = unsort[len(unsort) // 2]
    low, equal, more = [], [], []

    for number in unsort:
        if number < pivot:
            low.append(number)
        elif number == pivot:
            equal.append(number)
        elif number > pivot:
            more.append(number)

    return quick(low) + equal + quick(more)


lst = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

print(quick(lst))