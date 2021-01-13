from itertools import permutations
import copy
def solution(expression):
    stack2 = []
    def abc(heap, expression_list2):
        stack = []
        # print(heap, expression_list2, '123123')


        for j in range(len(heap)):
            flag = 1
            while flag != 0:
                flag = 0
                for i in range(1, len(expression_list2), 2):

                    if expression_list2[i] == heap[j]:
                        if heap[j] == '+':
                            k = expression_list2[i-1] + expression_list2[i+1]
                            expression_list2.pop(i-1)
                            expression_list2.pop(i-1)
                            expression_list2[i-1] = k
                            flag = 1
                            break

                        elif heap[j] == '*':
                            k = expression_list2[i-1] * expression_list2[i+1]
                            expression_list2.pop(i-1)
                            expression_list2.pop(i-1)
                            expression_list2[i-1] = k
                            flag = 1
                            break

                        elif heap[j] == '-':
                            k = expression_list2[i-1] - expression_list2[i+1]
                            expression_list2.pop(i-1)
                            expression_list2.pop(i-1)
                            expression_list2[i-1] = k
                            flag = 1
                            break

        stack2.append(abs(expression_list2[0]))
        print(expression_list2)


    answer = 0

    print(expression)
    expression_list = []
    count = 0
    for i in range(len(expression)):

        if expression[i] == '-' or  expression[i] == '*' or expression[i] == '+':
            expression_list.append(int(expression[count:i]))
            expression_list.append(expression[i:i+1])
            count = i+1
    expression_list.append(int(expression[count:len(expression)]))
    rank = ['-', '+', '*']

    k = list(permutations(rank,3))
    print(k)
    for i in range(len(k)):
        ex = copy.deepcopy(expression_list)
        abc(k[i], ex)


    print(stack2)



    return max(stack2)




expression = "100-200*300-500+20"
solution(expression)