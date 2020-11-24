def solution(array, commands):
    answer = []

    print(array, commands)
    new_array = []
    for i in range(len(commands)):
        new_array = array[commands[i][0]-1: commands[i][1]]
        new_array.sort()
        print(new_array)
        k = commands[i][2]
        print(k)

        answer.append(new_array[k-1])

    return answer


array = [1, 5, 2, 6, 3, 7, 4]
commands = 	[[2, 5, 3], [4, 4, 1], [1, 7, 3]]

solution(array,commands)