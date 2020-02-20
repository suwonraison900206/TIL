import sys
sys.stdin = open("dice.txt","r")

N, M, x, y, K = map(int, input().split())
mat = [list(map(int, input().split)) for _ in range(M)]
K_list = list(map(int, input().split()))
dice = [0]*7        #dice[0] 위치 찾을것

def num4() :
