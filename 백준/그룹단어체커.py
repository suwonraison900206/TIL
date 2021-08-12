import sys
sys.stdin = open('그룹단어체커.txt')

count = 0
for i in range(int(input())):

    words = list(input())
    words_dict = {}

    for word in words:
        words_dict[word] = 0

    check = ''
    flag = 0
    for word in words:
        # print(word, check)
        if not check:
            check = word
            words_dict[word] = 1
        else:
            if word == check:
                pass

            elif word != check:
                if words_dict[word] == 1:
                    flag = 1
                    break
                else:
                    check = word
                    words_dict[word] = 1

    if flag == 0:
        count +=1

print(count)






