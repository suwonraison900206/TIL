import sys
sys.stdin = open("dragon.txt")

t = int(input())

arr = [[0] * 100 for _ in range(100)]

print(arr)

for test_case in range(t):
    x, y, d, g = list(map(int,input().split()))


