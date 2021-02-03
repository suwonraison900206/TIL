from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = []
    cnt = 0
    for i in range(len(cities)):
        cities[i] = cities[i].upper()

    if cacheSize == 0:
        return 5 * len(cities)

    for i in cities:

        if i not in cache:


            if len(cache) == cacheSize:
                cache.pop(0)
                cache.append(i)
                cnt +=5
            else:
                cache.append(i)
                cnt +=5
        else:

            cache.pop(cache.index(i))
            cache.append(i)
            cnt +=1

    print(cnt)


    return cnt

cacheSize = 3
cities = ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']
solution(cacheSize,cities)