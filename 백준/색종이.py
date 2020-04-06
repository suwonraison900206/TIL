import sys
sys.stdin = open("color_paper.txt")


lst = []
for i in range(10):
    lst.append(list(map(int,input().split())))

visit_lst = [[0] * 10 for _ in range(10)]
visit_lst2 = [[0] * 10 for _ in range(10)]
visit_lst3 = [[0] * 10 for _ in range(10)]



result = 0

paper_5 = 0
paper_4 = 0
paper_3 = 0
paper_2 = 0
paper_1 = 0

paper_4_2 =0
paper_3_2 =0
paper_2_2 =0
paper_1_2 =0

paper_3_3 = 0
paper_2_3 = 0
paper_1_3 = 0






false_1 = 0

for i in range(6):
    for j in range(6):
        cnt = 0
        if lst[i][j] == 1:
            for q in range(5):
                for k in range(5):
                    if visit_lst[i + q][j + k] == 0:
                        cnt = cnt + lst[i+q][j+k]

                    if cnt == 25:
                        paper_5 = paper_5 + 1
                        for n in range(5):
                            for m in range(5):
                                visit_lst[i+n][j+m] = 1
for i in range(7):
    for j in range(7):
        cnt = 0
        if lst[i][j] == 1:
            for q in range(4):
                for k in range(4):
                    if visit_lst[i+q][j+k] == 0:
                        cnt = cnt + lst[i+q][j+k]
                    if cnt == 16:
                        paper_4 = paper_4 + 1
                        for n in range(4):
                            for m in range(4):
                                visit_lst[i + n][j + m] = 1
# 3x3
for i in range(8):
    for j in range(8):
        cnt = 0
        if lst[i][j] == 1:
            for q in range(3):
                for k in range(3):
                    if visit_lst[i+q][j+k] == 0:
                        cnt = cnt + lst[i+q][j+k]
                    if cnt == 9:
                        paper_3 = paper_3 + 1
                        for n in range(3):
                            for m in range(3):
                                visit_lst[i + n][j + m] = 1
# 2 x2
for i in range(9):
    for j in range(9):
        cnt = 0
        if lst[i][j] == 1:
            for q in range(2):
                for k in range(2):
                    if visit_lst[i+q][j+k] == 0:
                        cnt = cnt + lst[i+q][j+k]
                    if cnt == 4:
                        paper_2 = paper_2 + 1
                        for n in range(2):
                            for m in range(2):
                                visit_lst[i + n][j + m] = 1
# 1 x 1
for i in range(10):
    for j in range(10):
        if lst[i][j] == 1:
            if visit_lst[i][j] == 0:
                paper_1 = paper_1 + 1

if paper_5 < 6 and paper_4 < 6 and paper_3 < 6 and paper_2 < 6 and paper_1 < 6:
    result = paper_5 + paper_4 + paper_3 + paper_2 + paper_1
else:
    false_1 = false_1 + 1





for i in range(7):
    for j in range(7):
        cnt = 0
        if lst[i][j] == 1:
            for q in range(4):
                for k in range(4):
                    if visit_lst2[i + q][j + k] == 0:
                        cnt = cnt + lst[i+q][j+k]

                    if cnt == 16:
                        paper_4_2 = paper_4_2 + 1
                        for n in range(4):
                            for m in range(4):
                                visit_lst2[i+n][j+m] = 1
# 3x3
for i in range(8):
    for j in range(8):
        cnt = 0
        if lst[i][j] == 1:
            for q in range(3):
                for k in range(3):
                    if visit_lst2[i + q][j + k] == 0:
                        cnt = cnt + lst[i+q][j+k]
                    if cnt == 9:
                        paper_3_2 = paper_3_2 + 1
                        for n in range(3):
                            for m in range(3):
                                visit_lst2[i+n][j+m] = 1
# 2 x2
for i in range(9):
    for j in range(9):
        cnt = 0
        if lst[i][j] == 1:
            for q in range(2):
                for k in range(2):
                    if visit_lst2[i + q][j + k] == 0:
                        cnt = cnt + lst[i+q][j+k]
                    if cnt == 4:
                        paper_2_2 = paper_2_2 + 1
                        for n in range(2):
                            for m in range(2):
                                visit_lst2[i+n][j+m] = 1
# 1 x 1
for i in range(10):
    for j in range(10):
        if lst[i][j] == 1:
            if visit_lst2[i][j] == 0:
                paper_1_2 = paper_1_2 + 1

if paper_4_2 < 6 and paper_3_2 < 6 and paper_2_2 < 6 and paper_1_2 < 6:
    if result != 0 and result > paper_4_2 + paper_3_2 +paper_2_2 +paper_1_2:
        result = paper_4_2 + paper_3_2 +paper_2_2 +paper_1_2
    else:
        result = paper_4_2 + paper_3_2 + paper_2_2 + paper_1_2
else:
    false_1 = false_1 + 1




# 3x3
for i in range(8):
    for j in range(8):
        cnt = 0
        if lst[i][j] == 1:
            for q in range(3):
                for k in range(3):
                    if visit_lst3[i + q][j + k] == 0:
                        cnt = cnt + lst[i+q][j+k]
                    if cnt == 9:
                        paper_3_3 = paper_3_3 + 1
                        for n in range(3):
                            for m in range(3):
                                visit_lst3[i+n][j+m] = 1
# 2 x2
for i in range(9):
    for j in range(9):
        cnt = 0
        if lst[i][j] == 1:
            for q in range(2):
                for k in range(2):
                    if visit_lst3[i + q][j + k] == 0:
                        cnt = cnt + lst[i+q][j+k]
                    if cnt == 4:
                        paper_2_3 = paper_2_3 + 1
                        for n in range(2):
                            for m in range(2):
                                visit_lst3[i+n][j+m] = 1
# 1 x 1
for i in range(10):
    for j in range(10):
        if lst[i][j] == 1:
            if visit_lst3[i][j] == 0:
                paper_1_3 = paper_1_3 + 1



if paper_3_3 < 6 and paper_2_3 < 6 and paper_1_3 < 6:
    if result != 0 and result > paper_4_2 + paper_3_2 +paper_2_2 +paper_1_2:
        result = paper_4_2 + paper_3_2 +paper_2_2 +paper_1_2
    else:
        result = paper_4_2 + paper_3_2 + paper_2_2 + paper_1_2
else:
    false_1 = false_1 + 1

if false_1 == 3:
    print(-1)
else:
    print(result)


