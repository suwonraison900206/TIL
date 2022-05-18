import copy

def backtracking(word, x, y):

    print(word, x, y)

    if x == y:
        return

    # target = x * 2
    # if target < 10000:
    #     target = target % 10000
    #     backtracking(word + 'D', target, y)
    # else:
    #     backtracking(word + 'D', target, y)
    #
    # backtracking(word + 'S', target - 1, y)

    left_target = list(str(x))
    left_target2 = []
    for i in range(1, len(left_target)):
        left_target2.append(left_target[i])
    left_target2.append(left_target[0])
    left_target2 = int(''.join(left_target2))
    print(left_target2)
    right_target = list(str(x))
    right_target2 = []
    right_target2.append(right_target[-1])
    for i in range(len(right_target)-1):
        right_target2.append(right_target[i])

    right_target2 = int(''.join(right_target2))
    print(right_target2)

    pass
T = int(input())
lst = [list(map(int, input().split())) for _ in range(T)]
"""
D: D 는 n을 두 배로 바꾼다. 결과 값이 9999 보다 큰 경우에는 10000 으로 나눈 나머지를 취한다. 그 결과 값(2n mod 10000)을 레지스터에 저장한다.
S: S 는 n에서 1 을 뺀 결과 n-1을 레지스터에 저장한다. n이 0 이라면 9999 가 대신 레지스터에 저장된다.
L: L 은 n의 각 자릿수를 왼편으로 회전시켜 그 결과를 레지스터에 저장한다. 이 연산이 끝나면 레지스터에 저장된 네 자릿수는 왼편부터 d2, d3, d4, d1이 된다.
R: R 은 n의 각 자릿수를 오른편으로 회전시켜 그 결과를 레지스터에 저장한다. 이 연산이 끝나면 레지스터에 저장된 네 자릿수는 왼편부터 d4, d1, d2, d3이 된다.
"""

for x, y in lst:

    backtracking('', x, y)


