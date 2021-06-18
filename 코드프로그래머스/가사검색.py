
def solution(words, queries):
    answer = []
    words_dict = {}
    len_dict = {}
    a = {}


    for query in queries:
        a[query] =1

        result = []
        for t in range(len(query)):
            if query[t] == '?':
                result.append(t)

        if len(query) not in len_dict:
            len_dict[len(query)] = [result]
        else:

            if result in len_dict[len(query)]:
                pass
            else:
                len_dict[len(query)].append(result)

    print(a)
    for word in words:
        word2 = word[:]
        word3 = list(map(str, word2))
        if len(word3) not in len_dict:
            continue
        else:

            for w in len_dict[len(word3)]:
                word4 = word3[:]
                for u in w:
                    word4[u] = '?'

                word5 = ''.join(word4)
                if word5 not in a:
                    continue
                if word5 not in words_dict:
                    words_dict[word5] = 1
                else:
                    words_dict[word5] += 1
    print(words_dict)
    for query in queries:
        if query in words_dict:
            answer.append(words_dict[query])
        else:
            answer.append(0)
    print(answer)
    return answer


words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
solution(words, queries)