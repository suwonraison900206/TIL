def solution(arr1, arr2):
    b = len(arr1)
    a = len(arr2[0])

    answer = [[0 for col in range(a)] for row in range(b)]

    for i,value1 in enumerate(arr1): # 0 [1,2,3]
        for k,value2 in enumerate(value1): #1,2,3
                    for j in range(a):
                        answer[i][j] += arr1[i][k] * arr2[k][j]
    return answer