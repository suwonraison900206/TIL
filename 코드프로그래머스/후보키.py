from itertools import combinations

def check():
    pass

def solution(relation):

    a = (1,2,3)
    b = (2,3)

    stack = [i for i in range( len(relation[0]))]

    stack2 = []
    for i in range(1, len(relation)+1):
        for j in combinations(stack, i):
            stack2.append(j)

    print(stack2)
    compare_lst1 = []
    compare_lst2 = []
    final_lst = []
    print(relation)
    # for i in range(len(relation)):
    #
    #
    #     for j in range(len(stack2)):
    #         print(stack2[j])



    for i in range(len(stack2)):
        # print(stack2[i])
        # print(len(stack2[i]), 'len')
        for j in range(len(stack2[i])):
            for k in range(len(relation)):

                if k == 0:
                    compare_lst1.append(relation[k][stack2[i][j]])
                else:
                    compare_lst2.append(relation[k][stack2][i][j])
                    if compare_lst2 in compare_lst1:
                        pass
                    compare_lst2 = []
                pass



    answer = 0
    return answer



relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]

solution(relation)