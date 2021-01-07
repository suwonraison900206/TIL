def solution(arr):
    zero_result = []
    one_result = []
    def abc(x, y, arr):
        print(x,y , arr)
        one_count = 0
        zero_count = 0

        if abs(x[0] - x[1]) == 1:

            if arr[y[0]][x[0]] == 0:
                zero_result.append(0)
                return
            elif arr[y[0]][x[0]] == 1:
                one_result.append(1)
                return



        for i in range(y[0], y[1]):
            for j in range(x[0], x[1]):
                print(i,j, x,y ,'ij')
                if arr[i][j] == 1:
                    one_count += 1
                elif arr[i][j] == 0:
                    zero_count += 1

                if one_count !=0 and zero_count !=0:

                    abc((x[0], x[1] // 2), (y[0], y[1] // 2), arr)
                    abc((x[1] // 2, x[1]), (y[0], y[1] // 2), arr)
                    abc((x[0], x[1] // 2), (y[1] // 2,  y[1]), arr)
                    abc((x[1] // 2, x[1]), (y[1] // 2, y[1]), arr)
                    return
        if one_count == 0:
            zero_result.append(0)
            return
        else:
            one_result.append(1)
            return


    answer = []
    print(arr)
    one_count = 0
    zero_count = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == 1:
                one_count += 1
            elif arr[i][j] == 0:
                zero_count += 1

            if one_count != 0 and zero_count !=0:
                abc((0, len(arr)//2), (0, len(arr) //2) , arr)
                abc((len(arr) // 2, len(arr)), (0, len(arr) //2), arr)
                abc((0, len(arr) // 2), (len(arr) // 2, len(arr)), arr)
                abc((len(arr) // 2, len(arr)), (len(arr) // 2, len(arr)), arr)
                return
    if one_count == 0:
        zero_result.append(0)
        return
    else:
        one_result.append(0)
        return

    return answer




arr = [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]
solution(arr)