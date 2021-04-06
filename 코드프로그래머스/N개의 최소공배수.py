from math import gcd

def solution(arr):

    for i in range(1, len(arr)):

        arr[i] = arr[i-1] * arr[i] //gcd(arr[i-1], arr[i])


    return arr[-1]



arr = [3,4,9,16]
solution(arr)