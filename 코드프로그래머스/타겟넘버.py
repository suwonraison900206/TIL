def solution(numbers, target):
    def abc(number, count, target,numbers):
        if count == len(numbers)-1:
            if number == target:
                answer.append(123)
                return
            else:
                return

        abc(number + numbers[count+1], count+1, target,numbers)
        abc(number - numbers[count+1], count+1, target,numbers)




    answer = []

    abc(numbers[0], 0, target,numbers)
    abc(-numbers[0], 0, target,numbers)


    return len(answer)

numbers = [1,1,1,1]
target = 3
solution(numbers,target)