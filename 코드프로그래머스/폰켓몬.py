def solution(nums):
    k = len(nums) // 2
    a = len(set(nums))
    if a > k:
        answer = k
    elif k >= a:
        answer = a

    return answer


nums = [3,3,3,2,2,4]

solution(nums)