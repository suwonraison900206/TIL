





p = 'this'
t = 'this is a book~! this is a chair this is a computer there is a chair'
m = len(p)
n = len(t)

def BruteForce(p, t):
    i = 0
    j = 0
    while j < m and  i < n:
        if t[i] != p[j]:
            i = i - j
            j = -1
        i = i + 1
        j = j + 1
    if j == m :
        return i - m
    else:
        return - 1

print(BruteForce(p,t))