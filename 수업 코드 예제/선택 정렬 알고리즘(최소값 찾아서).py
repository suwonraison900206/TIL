def selectionsort(a) :
    for i in range(0, len(a)-1):
        min = i
        for j in range(i+1, len(a)):
            if a[min] > a[j] :
                min = j
        a[i], a[min] = a[min], a[i]
    return a



a = [2, 4, 7, 9, 11, 19, 23, 25, 13, 16]

print(selectionsort(a))