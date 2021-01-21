from itertools import combinations

def solution(nums):
    answer = -1
    print(nums)

    nums_list = [1] * 50000
    nums_list[0] = 0
    nums_list[1] = 0

    for i in range(2,len(nums_list)):

        if nums_list[i] == 1:

            for j in range(i * 2, len(nums_list), i):
                nums_list[j] = 0

    k = list(combinations(nums, 3))
    print(k)
    print(nums_list[0:50])
    cnt = 0
    for i in range(len(k)):

        count = k[i][0] + k[i][1] + k[i][2]
        print(count)
        if nums_list[count] == 1:
           cnt +=1
        else:
            pass
    print(cnt)

    return answer


nums = [1,2,3,4]
solution(nums)