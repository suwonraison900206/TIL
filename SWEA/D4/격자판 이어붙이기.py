import sys
sys.stdin = open("pan.txt")
sys.setrecursionlimit(10**6)

def up(x,y, k):
    global final_result
    global final_lst
    final_result.append(lst[x][y])
    print(final_result)
    if k == 7:
        print(final_result)
        final_result = []
    elif k < 7:
        if x - 1 >= 0:
            up(x - 1, y, k+1)
        if x + 1 < 3:
            down(x + 1, y, k+1)
        if y - 1 >= 0:
            left(x, y - 1, k+1)
        if y + 1 < 3:
            right(x, y + 1, k+1)
def down(x,y, k):
    global final_result
    global final_lst
    final_result.append(lst[x][y])
    if k == 7:
        print(final_result)
        final_result = []
    elif k < 7:

        if x - 1 >= 0:
            up(x - 1, y, k + 1)
        if x + 1 < 3:
            down(x + 1, y, k + 1)
        if y - 1 >= 0:
            left(x, y - 1, k + 1)
        if y + 1 < 3:
            right(x, y + 1, k + 1)


def left(x,y, k):
    global final_result
    global final_lst
    final_result.append(lst[x][y])

    if k == 7:
        print(final_result)
        final_result = []
    elif k < 3:
        if x - 1 >= 0:
            up(x - 1, y, k + 1)
        if x + 1 < 3:
            down(x + 1, y, k + 1)
        if y - 1 >= 0:
            left(x, y - 1, k + 1)
        if y + 1 < 3:
            right(x, y + 1, k + 1)


def right(x,y, k):
    global final_result
    global final_lst
    final_result.append(lst[x][y])

    if k == 7:
        print(final_result)
        final_result = []
    elif k < 7:
        if x - 1 >= 0:
            up(x - 1, y, k + 1)
        if x + 1 < 3:
            down(x + 1, y, k + 1)
        if y - 1 >= 0:
            left(x, y - 1, k + 1)
        if y + 1 < 3:
            right(x, y + 1, k + 1)


t = int(input())
for test_case in range(t):
    lst = []
    final_lst = []

    for i in range(3):
        number = list(map(int,input().split()))
        lst.append(number)

    final_result = []

    for i in range(3):
        for j in range(3):
            if i - 1 >= 0:
                final_result = []
                final_result.append(lst[i][j])
                up(i - 1, j, 2)
            if i + 1 < 3:
                final_result = []
                final_result.append(lst[i][j])
                down(i + 1, j, 2)
            if j - 1 >= 0:
                final_result = []
                final_result.append(lst[i][j])
                left(i, j - 1, 2)
            if j + 1 < 3:
                final_result = []
                final_result.append(lst[i][j])
                right(i, j + 1, 2)

    print(final_lst)

