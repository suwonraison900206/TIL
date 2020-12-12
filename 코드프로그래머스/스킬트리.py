def solution(skill, skill_trees):
    answer = 0
    skill = list(skill)



    for skill_tree in skill_trees:
        skill2 = skill[:]
        flag = 0
        for j in list(skill_tree):

            if j in skill2:
                if j != skill2[0]:

                    flag = 1
                    break
                elif j == skill2[0]:
                    skill2.pop(0)

        if flag == 0:
            answer += 1

    return answer


skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]

solution(skill, skill_trees)