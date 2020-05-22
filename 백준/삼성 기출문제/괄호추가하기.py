from itertools import combinations
import sys
sys.stdin = open('괄호추가하기.txt')
N = int(input())
number = list(input())
lst_1 = []
lst_2 = []


for i in range(N):
    try:
        lst_1.append(int(number[i]))
    except:
        lst_2.append(number[i])

print(lst_1)
print(lst_2)

for i in ran