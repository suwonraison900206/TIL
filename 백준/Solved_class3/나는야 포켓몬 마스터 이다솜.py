N, M = map(int,input().split())
N_lst =[list(input().split()) for __ in range(N)]
question =[list(input().split()) for __ in range(M)]
number = {}
word = {}
for i, v in enumerate(N_lst, start=1):
    number[i] = v[0]
    word[v[0]] = i

for q in question:
    try:
        print(number[int(q[0])])
    except:
        print(word[q[0]])
