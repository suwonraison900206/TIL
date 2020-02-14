cnt = 0
for i in range(4):
    for j in range(4):
        if i > j:
            print(' ' ,end='')
        if i <= j :
            cnt = cnt +1
            print(cnt,end=' ')
    print()