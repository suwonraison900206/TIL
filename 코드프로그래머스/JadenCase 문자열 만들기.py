def solution(s):
    print(s)
    answer =''
    word_list = list(s.split((' ')))


    for i in range(len(word_list)):
        word_list[i] = word_list[i].lower()
        word_list[i] = word_list[i].capitalize()
        if i == len(word_list) -1:
            answer = answer + word_list[i]
        else:

            answer = answer + word_list[i] + ' '

    print(str(answer))

    return answer

s = "3people unFollowed me"

solution(s)