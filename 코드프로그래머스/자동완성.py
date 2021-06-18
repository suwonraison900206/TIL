from pprint import pprint

def solution(words):
    answer = 0
    word_dict = {}
    result = []
    for word in words:
        next_dict = word_dict
        for string in word:

            if string not in next_dict:
                next_dict[string] = [1, {}]
            else:
                next_dict[string][0] += 1
            next_dict = next_dict[string][1]

    for word in words:
        next_dict = word_dict
        for string in word:
            answer += 1
            if next_dict[string][0] == 1:
                break
            next_dict = next_dict[string][1]

    print(answer)

words = ["word","war","warrior","world"]
solution(words)