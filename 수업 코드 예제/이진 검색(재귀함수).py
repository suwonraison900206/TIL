def binarysearch2(a, low, high, key):
    if low > high :
        return False
    else:
        middle = (low + high) // 2
        if key == a[middle]:
            return True
        elif key < a[middle]:
            return binarysearch2(a, low, middle-1, key)
        elif a[middle] < key :
            return binarysearch2(a, middle+1, high, key)

a = [2, 4, 7, 9, 11, 19, 23]

print(binarysearch2(a, 2, 19,11))
