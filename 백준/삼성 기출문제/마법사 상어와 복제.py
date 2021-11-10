import sys
sys.stdin = open('마법사 상어와 복제.txt')

import copy

M, S = map(int,input().split())
fishs = [list(map(int,input().split())) for _ in range(M)]
shark = list(map(int,input().split()))
