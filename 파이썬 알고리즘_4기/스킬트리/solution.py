def solution(skill, skill_trees):
    answer = 0
    skill = list(skill)

    for skill_tree in skill_trees:
        pointer = 0
        flag = 0
        for j in skill_tree:

            if j in skill:

                if j == skill[pointer]:
                    pointer +=1
                else:
                    flag = 1
                    break
        # for skill_tree in skill_trees:
        #     pointer = 0
        #
        #     for s in skill_tree:
        #         if s in skill:
        #             if s == skill[pointer]:
        #                 pointer += 1
        #             else:
        #                 break
        #     else:
        #         answer += 1
        #
        # return answer
        # for _ else 문 사용하면 flag 판단 변수 없이 판별 가능



        if flag == 0:
            answer +=1
    return answer


skill = "CBD"
skill_trees = ['BACDE', 'CBADF', 'AECB', 'BDA']
solution(skill, skill_trees)