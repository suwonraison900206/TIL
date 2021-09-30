A, B, V = map(int,input().split())

V -= A
C = A - B
D = V // C
E = V % C

if E != 0:
    print(D + 2)
else:
    print(D + 1)