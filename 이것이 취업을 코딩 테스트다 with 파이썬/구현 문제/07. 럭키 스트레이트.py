import sys
sys.stdin = open("07. 럭키 스트레이트.txt")

N = list(map(int,input()))
length = len(N)// 2
compare_a = N[0:length]
compare_b = N[length::]
count_a = 0
count_b = 0

for i in range(length):
    count_a = count_a + compare_a[i]
    count_b = count_b + compare_b[i]

if count_a == count_b:
    print("LUCKY")
else:
    print("READY")