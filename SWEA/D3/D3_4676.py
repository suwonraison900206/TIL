import sys
sys.stdin = open("4676.txt")

t = int(input())

for test_case in range(t):

    k = list(str(input()))
    H = int(input())
    cnt = list(map(int,input().split()))
    cnt.sort()
    while cnt:
        queue = cnt.pop(0)
        if queue == 0:
            k[queue] = '-' + k[queue]
        else:
            k[queue-1] = k[queue-1] + '-'


    result = ''.join(k)
    print('#{} {}'.format(test_case+1, result))

