a = []
b = []

# list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
#
# dx = [0, 0, -1, -1]
# dy = [-1, 1, 0, 0]
#
# test = []
# testX = 0
# testY = 0
#
#
# for x in range(len(list)):
#     for y in range(len(list[x])):
#         for i in range(4):
#             testX = x + dx[i]
#             testY = y + dy[i]
#             test = test(list[testX][testY])
#
# print(test)

M_list = []
for i in range(5):
    M_list.append(list(map(int, input().split())))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = 0
for x in range(5):
    for y in range(5):
        sum = 0
        for h in range(4):
            if x+dx[h] > -1 and y+dy[h] > -1 and x+dx[h] < 5 and y+dy[h] < 5:
                sum += abs(M_list[x][y] - M_list[x+dx[h]][y+dy[h]])
        result += sum
print(result)


#
# M_list = []
# for i in range(5):
#     M_list.append(list(map(int, input().split())))
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# result = 0
# for x in range(5):
#     for y in range(5):
#         for h in range(4):
#             if 0 <= x+dx[h] < 5 and 0 <= y+dy[h] < 5:
#                 result += abs(M_list[x][y] - M_list[x+dx[h]][y+dy[h]])







#
# for i in range(5):
#     for j in range(5):
#
#
