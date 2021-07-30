def solution(n, k, cmd):
    answer = ''

    print(n, k , cmd)

    dict1 = {}
    dict2 = {}

    for i in range(n):
        dict1[i] = [1]
        dict2[i] = ['O']


    target = k
    end = n-1
    save = []
    for i in cmd:
        check = i.split()
        print(check, target)
        if check[0] == 'D':
            target += int(check[1])

        elif check[0] == 'U':
            target -= int(check[1])

        elif check[0] == 'C':
            del dict1[end]
            end -=1
            dict2[target] = ['X']
            save.append(target)

        elif check[0] == 'Z':

            dict2[save[-1]] = ['O']
            save.pop()


    for key, value in dict2.items():

        answer = answer + value[0]

    return answer

n = 8
k= 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]

solution(n,k,cmd)