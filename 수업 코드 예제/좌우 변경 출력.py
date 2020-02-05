a_list = []
b_list = []
c_list = []
d_list = []
for i in range(25):
    a_list.append(i)
for i in range(5):
    b_list.append(a_list[i * 5:5 + (i * 5)])
# print(b_list)
for i in range(len(b_list)):
    if i % 2 == 1:
        c_list.append(b_list[i])
    # c_list = b_list[1::2]
for i in range(len(c_list)):
    d_list.append(c_list[i][::-1])
print(c_list)
print(d_list)
cnt = 0
for i in range(5):
    print()
    for j in range(5):
        if i  % 2 == 1:
            print(d_list[cnt][j],end='')
            if j == 4:
                cnt = cnt + 1
        else:
            print(b_list[i][j],end='')