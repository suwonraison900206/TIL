final_result = []

def solve(length, find, lst, result , end):

    if length == end-1:
        result = result + [find]
        final_result.append(result)

        return



    find_stack = []
    for i in range(len(lst)-1, -1, -1):
        if find == lst[i][0]:
            result.append(find)
            find_stack.append(lst[i][1])
            k = lst.pop(i)
            solve(len(result), find_stack[0], lst, result, end)
            result.pop(-1)
            lst.insert(i,k)
            find_stack = []


def solution(tickets):

    a = len(tickets) + 1

    answer = []
    stack = []

    for i in range(len(tickets)-1,-1,-1):
        if (tickets[i][0]) == 'ICN':
            answer.append('ICN')
            stack.append(tickets[i][1])
            k = tickets.pop(i)
            solve(len(answer), stack[0], tickets, answer, a)
            answer.pop()
            tickets.insert(i, k)
            stack = []

    final_result.sort()
    answer = final_result[0]
    return answer

# tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
solution(tickets)

final_result.sort()
print(final_result[0])

