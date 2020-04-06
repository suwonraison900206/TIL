
import sys
sys.stdin = open("reserch.txt")




K , N = list(map(int, input().split()))
temp =[]

for i in range(K):
    temp_k = list(map(int, input().split()))
    temp.append(temp_k)

print(temp)

test_list = []

for i in range(K):
    for j in range(N):
        if temp[i][j] == 0:
            test_list.append((i*N) + j)

n = test_list
final_list = []
for i in range(len(n)):
    for j in range(i+1, len(n)):
        for k in range(j+1, len(n)):
            sample_list = []
            if n[i] != n[j] and n[i] != n[k] and n[j] != n[k]:
                sample_list.append(n[i])
                sample_list.append(n[j])
                sample_list.append(n[k])
                final_list.append(sample_list)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

entry_x, entry_y = 0, 0

# print(final_list)
#
# print(len(final_list))
#


for i in range(len(final_list)):
    if final_list[i][0] == 0:
        temp[0][0] = 1
        if temp[final_list[i][1] // 6][final_list[i][1] % 6] == 1 and temp[final_list[i][2] // 6][final_list[i][2] % 6] == 1:
            for x in range(K):
                for y in range(N):





#
#
# n = len(test_list)
# final_list = []
#
#
#


# for i in range(1, 1<<n):
#     result = []
#     for j in range(n+1):
#         if i & (1<<j):
#             result.append(arr[j])
#             if len(result) == 3:
#                 print(result)
#     print()
# print()
#





# for i in range(len(test_list)):
#     for j in range(len(test_list)):
#         for k in range(len(test_list)):
#             if test_list[i] != test_list[j] and test_list[i] != test_list[k] and test_list[j] != test_list[k]:
#                 final_test.append([test_list[i], test_list[j], test_list[k]])
#                 print(final_test)
