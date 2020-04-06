import sys
sys.stdin = open("hide.txt")

N , K = list(map(int,input().split()))


def foward(a , time):
    global final_result

    if time > final_result:
        return
    if a == N:
        if time < final_result:
            final_result = time
            result.append(time)
    else:
        if K % 2 == 0:
            teleport((a / 2), time + 1)
        else:
            foward(a + 1, time + 1)
            backward(a - 1, time + 1)


def backward(a, time2):
    global final_result
    if time2 > final_result:
        return
    if a == N:
        if time2 < final_result:
            final_result = time2
            result.append(time2)
    else:
        if a % 2 == 0:
            teleport((a / 2), time2 + 1)
        else:
            foward(a + 1, time2 + 1)
            backward(a - 1, time2 + 1)

# 2 * N

def teleport(a, time3):
    global final_result

    if time3 > final_result:
        return
    if a == N:
        if time3 < final_result:
            final_result = time3
            result.append(time3)
    else:
        if a % 2 == 0:
            teleport((a / 2), time3 + 1)
        else:
            foward(a + 1, time3 + 1)
            backward(a - 1, time3 + 1)
final_result = 10000
result = []

if K % 2 == 0:
    teleport((K/ 2), 1)
else:
    foward(K + 1, 1)
    backward(K -1, 1)

print(result[-1])



from collections import deque
def bfs():
    q = deque() q.append(N)
    while q: v = q.popleft()
    if v == K: print(time[v])
    return
    for next_step in (v-1, v+1, v*2):
        if 0 <= next_step < MAX and not time[next_step]:
            time[next_step] = time[v] + 1
            q.append(next_step) MAX = 100001
            N, K = map(int, input().split()) time = [0]*MAX bfs()

출처: https://deepwelloper.tistory.com/75 [DEVLOG]