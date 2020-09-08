def solution(record):

    stack = []
    answer = []
    for i in range(len(record)):
        a = list(record[i].split())
        stack.append(a)
    final_result = []
    for i in range(len(stack)):
        if stack[i][0] == "Enter":

            if len(final_result) != 0:
                final_result.append([stack[i][0], stack[i][1], stack[i][2]])
                for j in range(len(final_result)):
                    if stack[i][1] == final_result[j][1]:
                        final_result[j][2] = stack[i][2]
            else:
                final_result.append([stack[i][0], stack[i][1], stack[i][2]])

        elif stack[i][0] == "Leave":
            for j in range(len(final_result)):
                if stack[i][1] == final_result[j][1]:
                    final_result.append([stack[i][0], stack[i][1], final_result[j][2]])
                    break
        elif stack[i][0] == "Change":
            for j in range(len(final_result)):
                if final_result[j][1] == stack[i][1]:
                    final_result[j][2] = stack[i][2]

    for i in range(len(final_result)):
        if final_result[i][0] == "Enter":
            answer.append(final_result[i][2] + "님이 들어왔습니다.")
        elif final_result[i][0] == "Leave":
            answer.append(final_result[i][2] +"님이 나갔습니다.")


    print(final_result)
    return answer



record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
solution(record)