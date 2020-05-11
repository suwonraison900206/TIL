import sys
sys.stdin = open('5201.txt')

T = int(input())

for test_case in range(T):
    N , M = map(int,input().split())
    W = list(map(int,input().split()))
    T_list = list(map(int,input().split()))
    W.sort(reverse=True)
    T_list.sort(reverse=True)


    count = 0
    while W:
        k = W.pop(0)

        if len(T_list) != 0:
            for i in range(len(T_list)):
                if T_list[i] >= k:
                    count = count + k
                    T_list.pop(i)
                    break
    print('#{} {}'.format(test_case+1,count))




