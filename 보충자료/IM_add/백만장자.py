'''
1 1 3 1 2

내가 산날 이후의 최고가에서 파는 것이 이득임

1 1 3 1 2       최고가     이득
       (2) ->    2          0
     (1)2  ->    2          1
    (3)12  ->    3          0
   (1)321  ->    3          2
 (1)1321   ->    3          2
                            -> 총 이득 : 5

최고가 = 마지막 날의 값

현재의 값이 최고가 보다 작으면
    팔아서 이득(최고가-현재가)을 남김
아니면
    최대값 = 현재값

'''

import sys
sys.stdin = open('input_백만.txt','r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    total_profit = 0    #총이득
    top_price =arr[N-1]         #마지막 날의 가격으로 최고가 초기화

    for i in range(N-1,-1,-1):  #뒤에서 부터 순회
        if arr[i]  < top_price:
            total_profit = total_profit + top_price-arr[i]
        else:
            top_price = arr[i]
    print('#{} {}'.format(tc,total_profit))














