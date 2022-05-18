def solution(enroll, referral, seller, amount):
    answer = []
    family = {}
    family_money = {}
    for member in enroll:
        if member not in family_money:
            family_money[member] = 0
    family_money['center'] = 0

    for mother, child in zip(enroll, referral):
        if child == '-':
            family[mother] = 'center'
        else:
            family[mother] = child

    for sell, money in zip(seller, amount):
        money = money * 100

        while True:
            if sell == 'center':
                family_money[sell] += money
                break
            else:
                a, b = round(money * 0.9) , round(money * 0.1)
                if b == 0:
                    family_money[sell] += money
                else:
                    family_money[sell] += a
                    rest_money = b

                sell = family_money[sell]
                money = rest_money

    for key, value in family_money.items():
        answer.append(value)

    answer.pop()

    return answer

enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]

referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]

solution(enroll,referral,seller,amount)
