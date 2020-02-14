import sys
sys.stdin = open("4828input.txt", "r")
a = int(input()) # 첫번째 입력값
result = []
for i in range(a):

    test_num = int(input()) #2번째로 입력받는 테스트케이스의 길이 입력 처리
    test_in = list(map(int, input().split()))#3번째로 입력받는 값 리스트로 바꾸는 처리(#2와 #3이 총 10번 반복됨)
    k = 0
    result2 = 0


    for i in range(len(test_in)-1, 0, -1):
        for j in range(0, i) :
            if test_in[j] > test_in[j+1]:
                test_in[j], test_in[j+1] = test_in[j+1], test_in[j]
                result2 = test_in[test_num -1] - test_in[0]

    k = k + 1
    result.append(result2)



for i in range(a):
    print('#{} {}'.format(i + 1, result[i]))