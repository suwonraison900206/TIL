import sys
import copy
sys.stdin = open('5203.txt')
import copy
def baby_gin(player, count, result):
    global number_list
    number_list2 = copy.deepcopy(number_list)
    player.sort()
    triplet = 1
    for i in range(len(player)):
        number_list2[player[i]] += 1
    if max(number_list2) >= 3:
        if result == 1:
            player1_result.append(count)
        elif result == 2:
            player2_result.append(count)
        return
    for i in range(len(player)-1):
        if triplet == 3:
            if result == 1:
                player1_result.append(count)
                return
            elif result == 2:
                player2_result.append(count)
                return

        elif player[i+1] - player[i] == 1:
            triplet += 1
        elif player[i+1] - player[i] == 0:
            pass
        elif player[i+1] - player[i] != 1 and player[i+1] - player[i] != 0 :
            triplet = 1


    if triplet == 3:
        if result == 1:
            player1_result.append(count)
        elif result == 2:
            player2_result.append(count)
    else:
        return

T = int(input())

for test_case in range(1,T+1):

    lst = list(map(int,input().split()))

    number_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    number_list2 = number_list[:]
    player1 = []
    player2 = []
    player1_result = []
    player2_result = []

    for i in range(len(lst)):
        if i % 2 == 0:
            player1.append(lst[i])
            if len(player1) >= 3:

                baby_gin(player1, len(player1), 1)

        else:
            player2.append(lst[i])
            if len(player2) >= 3:
                baby_gin(player2, len(player2), 2)


    if len(player1_result) == 0 and len(player2_result) == 0:
        print('#{} 0'.format(test_case))
    elif len(player1_result) != 0 and len(player2_result) == 0:
        print('#{} 1'.format(test_case))
    elif len(player1_result) == 0 and len(player2_result) != 0:
        print('#{} 2'.format(test_case))
    elif min(player1_result) < min(player2_result):
        print('#{} 1'.format(test_case))
    elif min(player1_result) > min(player2_result):
        print('#{} 2'.format(test_case))
    elif min(player1_result) == min(player2_result):
        print('#{} 1'.format(test_case))

