import sys
sys.stdin = open("possible_point.txt")

# def point(n, k, r):  # 0 , 0
#     if k == Num:
#         if r not in result:
#             result.append(r)
#     else:
#         point(n + 1, k+1, r)
#         point(n + 1, k+1, r + Number[n])


def calculate(lst, result):
    global please
    if result == Num:
        please = lst
    else:
        for i in range(len(cnt)):
            if cnt[i] + Number[result] not in cnt:
                cnt.append(cnt[i] + Number[result])
        calculate(cnt, result + 1)


t = int(input())
for test_case in range(t):
    Num = int(input())
    result = []
    Number = list(map(int,input().split()))
    n = 0
    # print('#{} {}'.format(test_case+1, len(result)))

    cnt = [0] + [Number[0]]

    please = []



    calculate(cnt, 1)
    print('#{} {}'.format(test_case+1,len(please)))



