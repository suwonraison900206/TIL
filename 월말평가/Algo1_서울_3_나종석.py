# import sys
# sys.stdin = open("number.txt")

T = int(input()) # 테스트 케이스
for test_case in range(T):
    a_time = int(input()) # 각 테스트 케이스별 이동 시간

    lst = list(map(int,input().split()))  # 입력 예시 받아 옵니다
    minus_lst =[0] * 10# 마이너스 규칙을 따를 리스트 를 만듭니다
    plus_lst =[0] * 10 # 플러스 규칙을 따를 리스트를 만듭니다.
    result_lst = [0] * 10

    for i in range(a_time): # 마이너스 값 계산 i ==0 일때는 규칙 3을 따르도록 제한
        for i in range(len(lst)):
            if lst[i] < 0 and lst[i] > -10:
                if i == 0:
                    minus_lst[i] += -(lst[i])
                elif i >= 1 and i <= 9:
                    minus_lst[i-1] = minus_lst[i-1] + lst[i]
                elif lst[i] <= -10:
                    minus_lst[i-1] += (-abs(lst[i]) //2)
                    plus_lst[i+1] += (abs(lst[i]) //2)
            if lst[i] <= -10:
                if i == 0:
                    minus_lst[i] += (abs(lst[i]) //2)
                    minus_lst[i + 1] += (abs(lst[i]) // 2)
                elif i > 0 and i < 9:
                    minus_lst[i-1] += (-abs(lst[i]) // 2)
                    minus_lst[i+1] += (abs(lst[i]) //2)
                elif i == 9:
                    minus_lst[i - 1] += (-abs(lst[i]) // 2)
                    minus_lst[i] += (-abs(lst[i]) // 2)


        for i in range(len(lst)): # 플러스 값 계산 10보다 클 경우 규칙 3 적용되도록 계산
            if lst[i] > 0 and lst[i] <= 9:
                if i >=0 and i <=8 :
                    plus_lst[i+1] = plus_lst[i+1] + lst[i]
                elif i == 9:
                    plus_lst[i] = plus_lst[i] -(lst[i])
            if lst[i] >= 10:
                if i == 0:
                    plus_lst[i] += (abs(lst[i]) //2)
                    plus_lst[i + 1] += (abs(lst[i]) // 2)
                elif i > 0 and i < 9:
                    plus_lst[i-1] += (-abs(lst[i]) // 2)
                    plus_lst[i+1] += (abs(lst[i]) //2)
                elif i == 9:
                    plus_lst[i - 1] += (-abs(lst[i]) // 2)
                    plus_lst[i] += (-abs(lst[i]) // 2)

        for i in range(len(lst)): # 마아너스 값 플러스 값 따로 계산한거 더해줍니다.
            lst[i] = plus_lst[i] + minus_lst[i]

        # 마이너스 , 플러스 리스트 초기화
        minus_lst =[0] * 10
        plus_lst = [0] * 10

    # 결과 출력
    print('#{} '.format(test_case+1),end='')
    for i in range(len(lst)):
        print(lst[i],end=' ')
    print()










