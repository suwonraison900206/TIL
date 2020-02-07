# 쥐쥐



t = int(input())


for test_case in range(t):

    a = list((input().split()))
    k = []
    for i in range(int(a[0])):

        b = list(map(int, input().split()))
        k.append(b)

    count = 0
    if a[1] == 'left' :
        for i in range(int(a[0]) -1, -1, -1 ):
            for j in range(int(a[0]) -1, 0, -1):
                if k[i][j] > k[i][j-1]:
                    k[i][j-1] = k[i][j]
                    k[i][j] = 0
                elif k[i][j] == k[i][j-1]:


                    k[i][j] = 0
                elif k[i][j] < k[i][j-1]:
                    k[i][j] = 0

    elif a[1] == 'right':
        for i in range(int(a[0])):
            for j in range(int(a[0])-1):
                if k[i][j] > k[i][j+1]:
                    k[i][j + 1] = k[i][j]
                    k[i][j] = 0
                elif k[i][j] == k[i][j+1]:
                    k[i][j+1] += k[i][j+1]
                    count = 1
                    if count == 1:
                        break

                    k[i][j] = 0
                elif k[i][j] < k[i][j+1]:
                    k[i][j] = 0
    elif a[1] == 'up':
        for i in range(int(a[0]) -1, 0, -1 ):
            for j in range(int(a[0]) -1, -1, -1):
                if k[i][j] > k[i-1][j]:
                    k[i-1][j] = k[i][j]
                    k[i][j] = 0
                elif k[i][j] == k[i-1][j]:

                    k[i][j] = 0
                elif k[i][j] < k[i-1][j]:
                    k[i][j] = 0

    elif a[1] == 'down':
        for i in range(int(a[0])-1):
            for j in range(int(a[0])):
                if k[i][j] > k[i+1][j]:
                    k[i+1][j] = k[i][j]
                    k[i][j] = 0
                elif k[i][j] == k[i+1][j]:

                    k[i][j] = 0
                elif k[i][j] < k[i+1][j]:
                    k[i][j] = 0

    print('#{} {}'.format(test_case + 1, k))

