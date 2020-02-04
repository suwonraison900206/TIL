num = 456789
c = [0] * 12

for i in range(6):
    c[num % 10] += 1
    num //= 10

i = 0
tri = run = 0

while i < 10 :
    if c[i] >= 3:  # triplet 조사 후 데이터 삭제
        c[i] -= 3
        tri += 1
    
    if c[i] >= 1 and c[i+1] >= c[i+2] >= 1: # run 조사 후 데이터 삭제
        c[i] -= 1
        c[i+1] -= 1
        c[i+2] -= 1
        run += 1

    i += 1
    
if run + tri == 2:
    print("baby gin")
else:
    print("lose")






