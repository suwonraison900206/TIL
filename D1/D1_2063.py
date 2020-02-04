# 중간값은 통계 집단의 수치를 크기 순으로 배열 했을 때 전체의 중앙에 위치하는 수치를 뜻한다.
#
# 입력으로 N 개의 점수가 주어졌을 때, 중간값을 출력하라.


a = int(input())

b = list(map(int, input().split(' ')))

for i in range(len(b)-1, 0, -1):
    for j in range(0, i):
        if b[j] > b[j+1]:
            b[j], b[j+1] = b[j+1], b[j]

print(b[(len(b) // 2)])


print(ord('A'))