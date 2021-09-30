import math

N, M = map(int,input().split())

a=math.gcd(N,M)
b= N* M // math.gcd(N,M)
print(a)
print(b)