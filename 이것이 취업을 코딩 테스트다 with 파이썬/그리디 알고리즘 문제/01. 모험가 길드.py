import sys
sys.stdin = open("01.모험가 길드.txt")


N = int(input())

hero = list(map(int,input().split()))
hero.sort()

count = 0
cnt = 0
number = 0
for i in range(len(hero)):
    if count == 0:
        count = hero[i] - 1
        number = hero[i]
        if count == 0:
            cnt = cnt + 1
    elif count != 0 and hero[i] <= number:
        count = count - 1
        if count == 0:
            cnt = cnt + 1
            pass
        pass
print (cnt)
