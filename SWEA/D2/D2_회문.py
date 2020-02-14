import sys
sys.stdin = open("풍선.txt")

t = int(input())



for test_case in range(t):
    N, M = map(int,input().split())
    temp = list(input().split()for _ in range(N))
    #
    # temp1 = temp[0]
    # print(temp1)
    # temp2 = temp1[0][0:10]
    # print(temp2)



    for i in range(N):
        for j in range(N-M+1):
            temp1 = temp[i]
            temp2 = temp1[i:i+10]

            print(temp1)
            print()
            print(temp2)

            temp3 = temp2[::-1]
            print()
            print(temp3)

            #
            # if temp2 == temp3:
            #     # print(temp3)
