
import sys
sys.stdin = open('1221.txt')


t = int(input())

for test_case in range(t):

    temp = list(map(str, input().split()))

    temp2 =list(map(str,input().split()))

    count_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    word_list =['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']


    for i in range(len(word_list)):
        for j in range(len(temp2)):
            if word_list[i] in temp2[j]:
                count_list[i] = count_list[i] + 1

    print(count_list)
    print('#{}'.format(test_case+1))
    for i in range(len(word_list)):
        for j in range(count_list[i]):
            print(word_list[i],end=' ')

        #
        # print('{}  '.format(word_list[i] * count_list[i]),end=' ')


