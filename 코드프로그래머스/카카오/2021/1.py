def solution(new_id):

    list = ['-', '_', '.', '0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    new_list = []
    last_word = new_id[-1]
    new_id = new_id.lower()

    for i in new_id:
        if i in list:

            new_list.append(i)



    for i in range(len(new_list)-1, 0, -1):

        if new_list[i] == '.' and new_list[i-1] == '.':
            new_list.pop(i)


    if len(new_list) !=0 and new_list[0] == '.':
        new_list.pop(0)

    if len(new_list) !=0 and new_list[-1] == '.':
        new_list.pop(-1)

    if len(new_list) == 0:
        new_list.append('a')
        last_word = 'a'
    if len(new_list) >= 16:
        new_list = new_list[0:15]
    if new_list[-1] == '.':
        new_list.pop(-1)

    if len(new_list) <= 2 :
        last_word = new_list[-1]
        k = 3 - len(new_list)
        for i in range(k):
            new_list.append(last_word)


    answer = "".join(new_list)

    return answer


