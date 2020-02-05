

test_in = list(map(int, input().split()))
test_in2 = []
result = []
for i in range(test_in[0]):
    test_in2.append(list(map(int, input().split())))

for i in range(0,3):
    for j in range(0,4):
        result.append(test_in2[i][j:test_in[1]+j])

print(result)
        #
        # result.append(test_in2[i-1][j-1] + test_in2[i][j-1] + test_in2[i-1][j] + test_in2[i][j])
        # print(result)
