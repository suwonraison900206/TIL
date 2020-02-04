result2 = []
for i in range(10):

    test_num = int(input()) #1번째 테스트 횟수
    test_in = list(map(int, input().split())) # 2번째 상자의 높이값
    k = 0
    

    while k < test_num :
        test_in_max = test_in[test_in.index(max(test_in))]
        test_in_min = test_in[test_in.index(min(test_in))]


        if test_in_max - test_in_min > 1:

            test_in[test_in.index(max(test_in))] -= 1
            test_in[test_in.index(min(test_in))] += 1
        k += 1
    
    result2.append(max(test_in) - min(test_in))
        
    


for i in range(10):
    print('#{0} {1}'.format(i+1 , result2[i]))