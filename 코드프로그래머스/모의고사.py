def solution(answers):

    num_1 =[1,2,3,4,5]
    num_2 =[2,1,2,3,2,4,2,5]
    num_3 =[3,3,1,1,2,2,4,4,5,5]
    answer = []
    k = len(answers)

    if k <= len(num_1):
        num_1 = num_1[:k]
    else:
        a = k // len(num_1)
        b = k % len(num_1)
        num_1 = (num_1 * a) + num_1[:b]
    if k <= len(num_2):
        num_2 = num_2[:k]
    else:
        a = k // len(num_2)
        b = k % len(num_2)
        num_2 = (num_2 * a) + num_2[:b]
    if k <= len(num_3):
        num_3 = num_3[:k]
    else:
        a = k // len(num_3)
        b = k % len(num_3)
        num_3 = (num_3 * a) + num_3[:b]


    stack =[0,0,0]

    for i in range(len(answers)):
        if answers[i] == num_1[i]:
            stack[0] = stack[0] + 1
        if answers[i] == num_2[i]:
            stack[1] = stack[1] + 1
        if answers[i] == num_3[i]:
            stack[2] = stack[2] + 1

    for i in range(len(stack)):
        if stack[i] == max(stack):
            answer.append(i+1)

    return answer


