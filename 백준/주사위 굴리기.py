temp = list(map(int, input().split()))

list_k = [[0] * temp[1] for _ in range(temp[0])]


for i in range(temp[0]):
    temp_k = list(map(int, input().split()))
    list_k[i][0] = temp_k[0]
    list_k[i][1] = temp_k[1]

move_list = list(map(int, input().split()))


print(list_k)
print(move_list)

