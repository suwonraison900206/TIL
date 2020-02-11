'''
1
2 2 2
3 4

1
2 2 2
1 2

0초 부터 붕어빵을 만들기 시작해서 M초에는 붕어빵 K개 만들 수 있음

손님은 그 다음에 주어진 시간에 찾아옴

손님이 올때 모든 손님이 붕어빵 먹으면 Possible
못먹으면 Imposible

2 2 2  : 2초 마다 붕어빵 2개 만듬
3 4    : 손님이 3,4초에 옴

시간 : 0 1 2 3 4 5 6 7 8 9
재고 : 0 0 2 2 4 4 6 6 8 8

=> 시간이 M의 배수일때 붕어빵이 K개 증가함

손님이 와서 붕어빵 겟
3,4
시간 : 0 1 2 3 4 5 6 7 8 9
재고 : 0 0 2 2 4 4 6 6 8 8
재고 : 0 0 2 1 3 3 5 5 7 7
재고 : 0 0 2 1 2 2 4 4 6 6

2 2 2
1 2

시간 : 0 1 2 3 4 5 6 7 8 9
재고 : 0 0 2 2 4 4 6 6 8 8
1초에 손님
재고 : 0 0 2 2 4 4 6 6 8 8

'''

T = int(input())
for tc in range(1,T+1):
    '''
    N : 손님수
    M : 붕어빵 만드는 시간
    K : 갯수
    '''
    N,M,K = map(int,input().split())
    customer = list(map(int,input().split()))

    remain = 0          #붕어빵 재고
    ans = 'Possible'    #가능여부
    
    #시간흐름으로 반복
    for i in range(11112):
        if i%M==0 and i!=0:
            remain+=K
        for c in customer:
            if c == i:
                if remain==0:
                    ans = "Impossible"
                    break
                remain-=1

    print('#{} {}'.format(tc, ans))

    










