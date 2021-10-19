from collections import deque

T = int(input())

for test in range(T):

    p = list(input())
    k = int(input())
    w = input()
    queue = deque()
    w = w.replace('[', '')
    w = w.replace(']', '')
    w = w.split(',')
    for i in w:
        try:
            queue.append(int(i))
        except:
            pass
    flag = True

    for word in p:

        if word == 'R':

            if flag == True:
                flag = False
            elif flag == False:
                flag = True
        elif word == 'D':

            if flag == True:
                if queue:
                    queue.popleft()
                else:
                    print('error')
                    break

            elif flag == False:
                if queue:
                    queue.pop()
                else:
                    print('error')
                    break
    else:
        if not queue:
            print('[]')
        else:

            queue = list(queue)
            if flag == False:
                queue = queue[::-1]
                a = '['
                for i, q in enumerate(queue):
                    if i == len(queue) -1:
                        a = a+str(q)
                    else:
                        a = a+str(q)+','
                a = a+']'
                print(a)
            else:
                a = '['
                for i,q in enumerate(queue):
                    if i == len(queue)-1:
                        a = a+str(q)
                    else:
                        a = a+str(q)+','
                a = a+']'

                print(a)
