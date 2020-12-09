def solution(w,h):

    square_lst = [[0] * w for __ in range(h)]
    print(square_lst)

    cnt_lst =[]
    cnt = w/h

    for i in range(h):
        cnt_lst.append((i, i * cnt))
    print(cnt_lst)


    print(cnt)



    answer = 1
    return answer

w = 8
h = 12

solution(w,h)