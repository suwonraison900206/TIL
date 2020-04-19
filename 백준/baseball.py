import sys
sys.stdin = open("baseball.txt")

def backtrack(a, k, N):
    c = [0] * N

    if k == N:

        soon_lst.append(a[:])
    else:
        in_perm = [False] * N
        for i in range(k):
            in_perm[a[i]] = True

        ncandidates = 0
        for i in range(N):
            if in_perm[i] == False:
                c[ncandidates] = i
                ncandidates += 1

        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k+1, N)

a = [0]*8
soon_lst = []
backtrack(a, 0, 8)

t = int(input())

result = []
result2 = []
choice = [0] * 10

for i in range(t):
    choice = [0] * 10
    player = list(map(int, input().split()))
    choice[4] = player[0]
    player.pop(0)
    result.append(player[:])
    result2.append(choice)

real_final_lst = []
for i in range(len(soon_lst)):
    stack = 1
    inning = [0] * 5
    for j in range(t):
        inning[0] = 0
        inning[1] = 0
        inning[2] = 0
        inning[3] = 0
        out = 0
        result2[j][1] = result[j][soon_lst[i][0]]
        result2[j][2] = result[j][soon_lst[i][1]]
        result2[j][3] = result[j][soon_lst[i][2]]
        result2[j][5] = result[j][soon_lst[i][3]]
        result2[j][6] = result[j][soon_lst[i][4]]
        result2[j][7] = result[j][soon_lst[i][5]]
        result2[j][8] = result[j][soon_lst[i][6]]
        result2[j][9] = result[j][soon_lst[i][7]]

        while (out < 3):
            if result2[j][stack] == 0:
                out = out + 1
            elif result2[j][stack] == 1:
                if inning[3] == 1:
                    inning[4] = inning[4] + 1
                    inning[3] = 0
                if inning[2] == 1:
                    inning[3] = 1
                    inning[2] = 0
                if inning[1] == 1:
                    inning[2] = 1
                    inning[1] = 0
                if inning[0] == 0:
                    inning[1] = 1
            elif result2[j][stack] == 2:
                if inning[3] == 1:
                    inning[4] = inning[4] + 1
                    inning[3] = 0
                if inning[2] == 1:
                    inning[4] = inning[4] + 1
                    inning[2] = 0
                if inning[1] == 1:
                    inning[3] = 1
                    inning[1] = 0
                if inning[0] == 0:
                    inning[2] = 1

            elif result2[j][stack] == 3:
                if inning[3] == 1:
                    inning[4] = inning[4] + 1
                    inning[3] = 0
                if inning[2] == 1:
                    inning[4] = inning[4] + 1
                    inning[2] = 0
                if inning[1] == 1:
                    inning[4] = inning[4] + 1
                    inning[1] = 0
                if inning[0] == 0:
                    inning[3] = 1

            elif result2[j][stack] == 4:
                if inning[3] == 1:
                    inning[4] = inning[4] + 1
                    inning[3] = 0
                if inning[2] == 1:
                    inning[4] = inning[4] + 1
                    inning[2] = 0
                if inning[1] == 1:
                    inning[4] = inning[4] + 1
                    inning[1] = 0
                if inning[0] == 0:
                    inning[4] = inning[4] + 1

            stack = stack + 1
            if stack == 10:
                stack = 1

        real_final_lst.append(inning[4])


print(max(real_final_lst))
