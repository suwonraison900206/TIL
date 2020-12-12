def solution(n):
    answer = []

    triangle = []


    for i in range(1,n+1):
        triangle.append([0] * (n -(n-i)))

    i = 0
    j = 0
    count = 1
    flag = 0

    if n == 1:
        return [1]
    while True:
        triangle[i][j] = count
        count += 1
        if flag == 0:
            if 0 <= i+1 <= n-1 and triangle[i+1][j] ==0:
                i = i + 1
            elif i == n-1 and triangle[i][j+1] == 0:
                flag = 1
                j = j +1

            elif 0 <= i+1 <= n-1 and triangle[i+1][j] !=0 and triangle[i][j+1] == 0:
                flag = 1
                j = j + 1
            else:
                break

        elif flag == 1:
            if 0 <= j + 1 <= n - 1 and triangle[i][j+1] == 0:
                j = j + 1
            elif j == n - 1 and triangle[i-1][j -1] == 0:
                flag = 2
                i = i-1
                j = j-1


            elif 0 <= j + 1 <= n - 1 and triangle[i][j+1] !=0 and triangle[i-1][j-1] ==0:
                flag =2
                i = i-1
                j = j-1
            else:
                break
        elif flag == 2:
            if 0 <= i - 1 <= n - 1 and 0 <= j - 1 <= n - 1 and triangle[i - 1][j -1] == 0:
                i = i -1
                j = j -1
            elif 0 <= i - 1 <= n - 1 and 0 <= j - 1 <= n - 1 and triangle[i-1][j-1] !=0 and triangle[i+1][j] == 0:
                flag = 0
                i = i +1
            else:
                break


    for i in range(len(triangle)):
        for j in range(len(triangle[i])):
            answer.append(triangle[i][j])



    return answer


n = 1

solution(n)