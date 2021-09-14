
def solution(money):
    answer = 0
    answer2 = 0
    money_lst = [0] * len(money)
    money_lst2 = [0] * len(money)
    money_lst[0] = money[0]

    for i in range(1, len(money)):

        if i == 1:
            money_lst[i] = max(money[i], money[i - 1])
            money_lst2[i] = max(money[i], money[i - 1])
        else:
            money_lst[i] = max(money_lst[i-2]+money[i] , money_lst[i-1])
            money_lst2[i] = max(money_lst2[i - 2] + money[i], money_lst2[i - 1])

    print(max(max(money_lst) , max(money_lst2)))
    return max(max(money_lst) , max(money_lst2))

money = [1,2,3,1,4]
solution(money)