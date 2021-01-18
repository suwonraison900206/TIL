

def getNumberOfOptions(priceOfJeans, priceOfShoes, priceOfSkirts, priceOfTops, budgeted):
    stack = []

    def shoe(money, budget):

        if money >= budget:
            return
        else:
            for i in range(len(priceOfShoes)):
                skirt(money + priceOfShoes[i], budget)

    def skirt(money, budget):
        if money >= budget:
            return
        else:
            for i in range(len(priceOfSkirts)):
                Top(money + priceOfSkirts[i], budget)

    def Top(money, budget):
        if money >= budget:
            return
        else:
            for i in range(len(priceOfTops)):
                if money + priceOfTops[i] <= budget:
                    stack.append('pass')



    for i in range(len(priceOfJeans)):

        shoe(priceOfJeans[i], budgeted)

    print(stack)d

    return stack

priceOfJeans = [4]
priceOfShoes = [3,4,1]
priceOfSkirts = [3,2]
priceOfTops = [4]
budgeted = 12

getNumberOfOptions(priceOfJeans, priceOfShoes, priceOfSkirts, priceOfTops, budgeted)