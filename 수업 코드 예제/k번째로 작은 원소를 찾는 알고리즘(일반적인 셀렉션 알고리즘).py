

# 1 번부터 k번째까지 작은 원소들을 찾아 배열의 앞쪽으로 이동시키고, 배열의 k번째를 반환한다
# k 가 비교적 작을 때 유용하여 O(kn)의 수행시간을 필요로 한다

def select(list, k):
    for i in range(0, k):
        minindex = i
        for j in range (i+1, len(list)):
            if list[minindex] > list[j]:
                minindex = j
        list[i], list[minindex] = list[minindex], list[i]
    return list[k-1]