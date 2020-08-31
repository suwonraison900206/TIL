

s = input()
s = sorted(s)
list_num = []
list_str = []
num_sum = 0
for i in s:
    if i.isnumeric()==False:
        list_str.append(i)
    else :
        num_sum += int(i)
        list_num.append(num_sum)

final_list = []
result =''.join(list_str)+str(num_sum)

print(result)