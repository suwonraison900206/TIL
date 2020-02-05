for tc in range (1, TC+1):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(N):
        found = False
        for j in range(N):
            if arr[i * 2] == arr[j * 2 + 1]:
                found = True
                break
        if found == False:
            start_position = i
            break


    arr[0], arr[start_position * 2] = arr[start_position * 2], arr[0]