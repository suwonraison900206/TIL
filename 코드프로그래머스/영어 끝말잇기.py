def solution(n, words):
    answer = []
    check_list = []

    L = len(words)

    idx = 0
    circle = 1

    for word in words:
        idx +=1
        if idx == n+1:
            idx = 1
            circle +=1
        if not check_list:
            check_list.append(word)
        else:
            if word[0] == check_list[-1][-1] and word not in check_list:
                check_list.append(word)

            else:
                return [idx, circle]

    return [0, 0]

n = 2
words = ["hello", "one", "even", "never", "now", "world", "draw"]
print(solution(n, words))