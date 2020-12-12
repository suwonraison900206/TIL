from itertools import combinations, permutations
import math
def solution(numbers):
    answer = 0

    k_list = [i for i in range(10**(len(numbers)))]
    k_list[1] = 0


    for i in range(2, len(k_list)):
        sqrt = int(math.sqrt(i))
        if k_list[i] !=0:
            u = i
            while u+i < len(k_list):
                u = u + i
                k_list[u] = 0

    numbers = list(numbers)
    r = []
    for i in range(1,len(numbers)+1):
        r = r + list(permutations(numbers, i))
    final_result = []
    for i in range(len(r)):
        Q = int((''.join(r[i])))

        if Q != 0 and Q != 1 and Q not in final_result:
            final_result.append(Q)
            if Q in k_list:
                answer +=1

    return answer

numbers = "17"
solution(numbers)