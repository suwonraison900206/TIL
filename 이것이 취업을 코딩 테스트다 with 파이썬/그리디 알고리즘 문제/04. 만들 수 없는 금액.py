import sys
sys.stdin = open("04. 만들 수 없는 금액.txt")

N = int(input())

coin = list(map(int,input().split()))

coin.sort()

print(coin)

target = 1

for num in coin:
    if target < num:
        break
    else:
        target = target + num

print(target)