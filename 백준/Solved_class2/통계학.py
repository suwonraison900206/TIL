from collections import Counter

N = int(input())
target = [int(input()) for __ in range(N)]
target.sort()
average = 0
mid = target[len(target)//2]
number_min = Counter(target)
rnge = target[-1] - target[0]


for i in target:

    average += i

average = round(average / len(target))
number_min = number_min.most_common(2)
print(average)
print(mid)
if len(number_min) == 1:
    print(number_min[0][0])
else:
    print(number_min[0][0] if number_min[0][1] != number_min[1][1] else number_min[1][0])
print(rnge)