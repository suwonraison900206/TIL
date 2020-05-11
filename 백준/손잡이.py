def solution(numbers, hand, phone, right, left):
    global result
    right_distance = 0
    left_distance = 0

    for i in range(len(numbers)):
        if numbers[i] == 1:
            left = (0,0)
            result.append('L')

        elif numbers[i] == 2:
            left_distance = abs((left[0] - 0)) + abs((left[1] - 1))
            right_distance = abs((right[0] - 0)) + abs((right[1] - 1))
            if left_distance < right_distance:
                left = (0, 1)
                result.append('L')
            elif left_distance > right_distance:
                right = (0, 1)
                result.append('R')
            elif left_distance == right_distance:
                if hand == 'right':
                    right = (0, 1)
                    result.append('R')
                elif hand == 'left':
                    left = (0, 1)
                    result.append('L')

        elif numbers[i] == 3:

            right = (0, 2)
            result.append('R')


        elif numbers[i] == 4:
            left = (1, 0)
            result.append('L')

        elif numbers[i] == 5:
            left_distance = abs((left[0] - 1)) + abs((left[1] - 1))
            right_distance = abs((right[0] - 1)) + abs((right[1] - 1))
            if left_distance < right_distance:
                left = (1, 1)
                result.append('L')
            elif left_distance > right_distance:
                right = (1, 1)
                result.append('R')
            elif left_distance == right_distance:
                if hand == 'right':
                    right = (1, 1)
                    result.append('R')
                elif hand == 'left':
                    left = (1, 1)
                    result.append('L')

        elif numbers[i] == 6:

            right = (1, 2)
            result.append('R')

        elif numbers[i] == 7:
            left = (2, 0)
            result.append('L')

        elif numbers[i] == 8:
            left_distance = abs((left[0] - 2)) + abs((left[1] - 1))
            right_distance = abs((right[0] - 2)) + abs((right[1] - 1))
            if left_distance < right_distance:
                left = (2, 1)
                result.append('L')
            elif left_distance > right_distance:
                right = (2, 1)
                result.append('R')
            elif left_distance == right_distance:
                if hand == 'right':
                    right = (2, 1)
                    result.append('R')
                elif hand == 'left':
                    left = (2, 1)
                    result.append('L')

        elif numbers[i] == 9:

            right = (2, 2)
            result.append('R')

        elif numbers[i] == 0:
            left_distance = abs((left[0] - 3) + (left[1] - 1))
            right_distance = abs((right[0] - 3) + (right[1] - 1))
            if left_distance < right_distance:
                left = (3, 1)
                result.append('L')
            elif left_distance > right_distance:
                right = (3, 1)
                result.append('R')
            elif left_distance == right_distance:
                if hand == 'right':
                    right = (3, 1)
                    result.append('R')
                elif hand == 'left':
                    left = (3, 1)
                    result.append('L')




    return

numbers =[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
hand = "right"
result =  []
right = (3,2)
left = (3,0)

phone_lst = [[1,2,3], [4,5,6], [7,8,9], ['*', 0, '#']]

solution(numbers, hand, phone_lst, right, left)

print(result)