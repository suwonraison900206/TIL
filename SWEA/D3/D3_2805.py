import sys
sys.stdin = open("2805.txt")




def farm(k, n):
    num = -1
    sum = 0
    for x in range(k//2+1):
        num += 1
        for y in range(k//2-num, k//2+num+1):
            sum += int(n[x][y])
    for x in range(k//2+1, k):
        num -= 1
        for y in range(k//2-num, k//2+num+1):
            sum += int(n[x][y])
    return sum
T = int(input())
for t in range(1, T+1):
    N = int(input())
    n_list = []
    for _ in range(N):
        n_list.append(input())
    print('#{} {}'.format(t, farm(N, n_list)))