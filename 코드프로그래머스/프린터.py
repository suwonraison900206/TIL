from collections import deque


def solution(priorities, location):
    answer = 0
    locate_stack = deque([i for i in range(len(priorities))])
    stack = deque(priorities)
    cnt = 0

    while True:
        priority = stack.popleft()
        locate = locate_stack.popleft()

        if not stack:  # 2, 5, 8 런타임 에러 : 스택이 비어있을때 max 값 뽑을수 없어서
            return cnt + 1


        if max(stack) > priority:

            stack.append(priority)
            locate_stack.append(locate)

        else:
            cnt += 1
            if locate == location:
                print(cnt)
                return cnt



priorities = [1]
location = 0

solution(priorities, location)