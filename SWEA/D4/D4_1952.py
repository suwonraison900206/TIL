import sys
sys.stdin = open("1952.txt")


t = int(input())

for test_case in range(t):

    FEE = list(map(int,input().split()))
    MONTH = list(map(int,input().split()))