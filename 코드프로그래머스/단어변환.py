def solution(begin, target, words):

    print(begin , target , words)

    stack =[begin]
    stack2 = []
    stack3 = [begin]
    cnt = 0
    while True:
        cnt +=1

        for i in range(len(words)):


            for q in range(len(stack)):
                flag = 0
                for j in range(len(words[i])):


                    if words[i][j] == stack[q][j]:
                        flag +=1

            if flag == len(begin)-1:

                if words[i] == target:
                    print(words[i], cnt, target)
                    return cnt
                if words[i] in stack3:
                    continue

                else:
                    stack2.append(words[i])
                    stack3.append(words[i])
        if len(stack2) == 0:
            return 0

        stack = stack2[:]
        stack2 = []



    answer = 0
    return answer

begin = "hit"
target = "cog"
words = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']

solution(begin, target, words)