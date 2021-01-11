def solution(land):
    answer = 0

    print(land)


    for i in range(1, len(land)):
        for j in range(len(land[i])):

            land[i][j] = land[i][j] + max(land[i-1][:j] + land[i-1][j+1:])

    print(max(land[len(land)-1]))


    return max(land[len(land)-1])


land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]

solution(land)