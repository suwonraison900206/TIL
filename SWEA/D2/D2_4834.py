import sys
sys.stdin = open("4828input.txt", "r")
a = int(input()) # 첫번째 입력값
result = []
for i in range(a):

    test_num = int(input()) #2번째로 입력받는 테스트케이스의 첫 줄에 카드 장수 N이 주어진다.
    test_in = list(map(int, input().split()))#3번째로 입력받는 값 리스트로 바꾸는 처리(#2와 #3이 총 10번 반복됨)

    vec = [0] * test_num
    mid = [0] * test_num
    cnt = [0] * test_num

    for i in range(0, len(mid)):
        cnt[vec[i]] += 1

    for i in range (1, len(cnt)):
        cnt[i] += cnt[i-1]

    for i in range (len(mid)-1, -1, -1) :
        mid[cnt[vec[i]]-1] = vec[i]
        cnt[vec[i]] -= 1





for i in range(a):
    print('#{} {}'.format(i + 1, result[i]))