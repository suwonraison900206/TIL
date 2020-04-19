import copy
import sys
sys.stdin = open("number.txt")

def perm(arr, k, N):
    global final_result
    if k == N:
        a = copy.deepcopy(arr)
        if a not in final_result:
            final_result.append(a)
    else:
        for i in range(k, N):
                arr[k], arr[i] = arr[i], arr[k]
                perm(arr, k + 1, N)
                arr[k], arr[i] = arr[i], arr[k]

t = int(input())

for test_case in range(t):
    num = int(input())
    list_k = list(map(int, input().split()))
    number_k = list(map(int, input().split()))
    arr = []
    cnt = 0
    for i in range(len(list_k)):
        while list_k[i]:
            arr.append(i+1)
            list_k[i] -= 1
            cnt = cnt + 1

    final_result = []

    perm(arr, 0, len(arr))

    min_max = []

    for i in range(len(final_result)):
        result = 0
        for j in range(len(number_k) -1):
            if j == 0:
                if final_result[i][j] == 1:
                    result = result + (number_k[j] + number_k[j+1])
                elif final_result[i][j] == 2:
                    result = result + (number_k[j] - number_k[j+1])
                elif final_result[i][j] == 3:
                    result = int(result + (number_k[j] * number_k[j+1]))
                elif final_result[i][j] == 4:
                    result = int(result + (number_k[j] / number_k[j+1]))
            else:
                if final_result[i][j] == 1:
                    result = result + number_k[j+1]
                elif final_result[i][j] == 2:
                    result = result - number_k[j+1]
                elif final_result[i][j] == 3:
                    result = int(result * number_k[j+1])
                elif final_result[i][j] == 4:
                    result = int(result / number_k[j+1])
        min_max.append(result)

    print('#{} {}'.format(test_case+1,max(min_max) - min(min_max)))
