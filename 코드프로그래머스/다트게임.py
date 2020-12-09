def solution(dartResult):
    dartResult = dartResult.replace('10', 'k')
    ing = []

    for i in dartResult:
        ing.append(i)

    for i in range(len(ing)):
        if ing[i] == "k":
            ing[i] = "10"

    for i in range(len(ing)):
        try:
            ing[i] = int(ing[i])
        except ValueError:
            pass
    if type(ing[1]) == str and type(ing[2]) == int:
        ing.insert(2, "@")
    if type(ing[4]) == str and type(ing[5]) == int:
        ing.insert(5, "@")
    if len(ing) == 8:
        ing.append("@")

    for i in range(len(ing)):
        if ing[i] == "S":
            ing[i] = 1
        if ing[i] == "D":
            ing[i] = 2
        if ing[i] == "T":
            ing[i] = 3

    score = []

    for i in range(3):
        score.append(ing[i*3]**ing[i*3+1])

    if ing[2] == "*":
        score[0] *= 2
    elif ing[2] =="#":
        score[0] *= -1

    if ing[5] == "*":
        score[0] *= 2
        score[1] *= 2
    elif ing[5] =="#":
        score[1] *= -1

    if ing[8] == "*":
        score[1] *= 2
        score[2] *= 2
    elif ing[8] =="#":
        score[2] *= -1

    return sum(score)