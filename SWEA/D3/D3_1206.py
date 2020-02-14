import sys
sys.stdin = open("1206input.txt", "r")

test_case = 10 # 문제에 써있는 테스트 케이스 갯수
result = []
for i in range(test_case):
    test_num = int(input()) #2번째로 입력받는 테스트케이스의 길이 입력 처리
    test_in = list(map(int, input().split()))#3번째로 입력받는 값 리스트로 바꾸는 처리(#2와 #3이 총 10번 반복됨)
    k = 2
    second_max = 0
    result2 = 0
    while k <= test_num -3:
        second_max = max(test_in[k-2], test_in[k-1], test_in[k+1], test_in[k+2])
        if test_in[k] <= second_max:
            k = k + 1
        else:
            result2 = result2 + (test_in[k] - second_max)
            k = k + 1
    result.append(result2)
for i in range(test_case):
    print('#{} {}'.format(i + 1, result[i]))










#
#
#
# a = 10 # 문제에 써있는 테스트 케이스 갯수
# result = []
# for i in range(a):
#     test_num = int(input()) #2번째로 입력받는 테스트케이스의 길이 입력 처리
#     test_in = list(map(int, input().split()))#3번째로 입력받는 값 리스트로 바꾸는 처리(#2와 #3이 총 10번 반복됨)
#     k = 2
#     check = 0
#     result_apt = 0
#     while k <= test_num-3:
#         check = max(test_in[k-2], test_in[k-1], test_in[k+1], test_in[k+2])
#         if test_in[k] <= check:
#             k += 1
#         elif test_in[k] > check:
#             result_apt += (test_in[k] - check)
#             k += 3
#     result.append(result_apt)
# for i in range(a):
#     print('#{} {}'.format(i+1, result[i]))
#
#





#
# a = 10 # 문제에 써있는 테스트 케이스 갯수
# result = []
# for i in range(a):
#     test_num = int(input()) #2번째로 입력받는 테스트케이스의 길이 입력 처리
#     test_in = list(map(int, input().split()))#3번째로 입력받는 값 리스트로 바꾸는 처리(#2와 #3이 총 10번 반복됨)
#
# for i in range(a):
# print('#{} {}'.format(i+1, result[i]))




