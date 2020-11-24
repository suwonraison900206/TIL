import sys
sys.stdin = open("마법사상어와파이어볼.txt")


N, M, K = map(int,input().split())

fireball_lst = [list(map(int,input().split())) for __ in range(M)]
fireball_lst2 = []
# r, c  = 파이어볼 위치, m = 질량 ,s= 속력 ,d = 방향

direction_lst = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

for i in range(K):


    for j in range(len(fireball_lst)):

        r, c, m, s, d = fireball_lst[j][0], fireball_lst[j][1], fireball_lst[j][2], fireball_lst[j][3], fireball_lst[j][4]

        r = r + (direction_lst[d][0] * s)
        c = c + (direction_lst[d][1] * s)


        if r > N:
            r = r % N
        elif r <= 0:
            while r <= 0:
                r = r + N

        if c > N:
            c = c % N
        elif c <= 0:
            while c <= 0:
                c = c + N

        fireball_lst[j] = [r,c,m,s,d]

    stack = []
    stack2 = []

    while fireball_lst:

        k = fireball_lst.pop()
        flag = 0
        if fireball_lst:
            for j in range(len(fireball_lst)):

                if k[0] == fireball_lst[j][0] and k[1] == fireball_lst[j][1]:
                    flag = 1
                    fireball_lst[j][2] += k[2]
                    fireball_lst[j][3] += k[3]

                    if (k[4] % 2 == 1 and fireball_lst[j][4] % 2 == 1):

                        fireball_lst[j].append('odd')

                    elif (k[4] % 2 == 0 and fireball_lst[j][4] % 2 == 0):

                        fireball_lst[j].append('even')
                    else:
                        fireball_lst[j].append('else')

            if flag == 0:
                fireball_lst2.append(k)
                cnt = 1
        else:
            fireball_lst2.append(k)
            cnt = 1

    fireball_lst = fireball_lst2[:]
    fireball_lst2 = []

    while fireball_lst:
        q = fireball_lst.pop()
        if len(q) != 5:
            odd_flag = 0
            even_flag = 0
            else_flag = 0
            for j in range(5, len(q)):
                if q[j] == 'odd':
                    odd_flag +=1
                elif q[j] == 'even':
                    even_flag +=1
                else:
                    else_flag +=1

            if else_flag != 0:
                if int(q[2]/5) >= 1:
                    fireball_lst2.append([q[0], q[1], int(q[2]/ 5), int(q[3] / (len(q) -4)), 1])
                    fireball_lst2.append([q[0], q[1], int(q[2] / 5), int(q[3] /(len(q) -4)), 3])
                    fireball_lst2.append([q[0], q[1], int(q[2] / 5), int(q[3] /(len(q) -4)), 5])
                    fireball_lst2.append([q[0], q[1], int(q[2] / 5), int(q[3] /(len(q) -4)), 7])
            elif (even_flag == 0 and odd_flag != 0) or (even_flag != 0 and odd_flag ==0):
                if int(q[2]/5) >= 1:
                    fireball_lst2.append([q[0], q[1], int(q[2]/ 5), int(q[3] /(len(q) -4)), 0])
                    fireball_lst2.append([q[0], q[1], int(q[2] / 5), int(q[3] /(len(q) -4)), 2])
                    fireball_lst2.append([q[0], q[1], int(q[2] / 5), int(q[3] /(len(q) -4)), 4])
                    fireball_lst2.append([q[0], q[1], int(q[2] / 5), int(q[3] /(len(q) -4)), 6])
        else:
            fireball_lst2.append(q)


    fireball_lst = fireball_lst2[:]
    fireball_lst2 = []



count = 0
if fireball_lst:
    for j in range(len(fireball_lst)):
        count = count + fireball_lst[j][2]
else:
    count = 0

print(count)






















