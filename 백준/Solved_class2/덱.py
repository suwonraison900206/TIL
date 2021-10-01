from collections import deque


N = int(input())
lst = [list(input().split()) for __ in range(N)]
queue = deque()
print(N, lst)
"""
push_front X: 정수 X를 덱의 앞에 넣는다.
push_back X: 정수 X를 덱의 뒤에 넣는다.
pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 덱에 들어있는 정수의 개수를 출력한다.
empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
"""
for i in lst:

    if i[0] == 'push_front':
        queue.appendleft(i[1])

    elif i[0] == 'push_back':
        queue.append(i[1])

    elif i[0] == 'pop_front':
        if not queue:
            print(-1)
        else:
            print(queue.popleft())

    elif i[0] == 'pop_back':
        if not queue:
            print(-1)
        else:
            print(queue.pop())

    elif i[0] == 'size':
        if not queue:
            print(0)
        else:
            print(len(queue))

    elif i[0] == 'empty':
        if not queue:
            print(1)
        else:
            print(0)

    elif i[0] == 'front':
        if not queue:
            print(-1)
        else:
            print(queue[0])

    elif i[0] == 'back':
        if not queue:
            print(-1)
        else:
            print(queue[-1])
