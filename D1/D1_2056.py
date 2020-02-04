# 연월일 순으로 구성된 8자리의 날짜가 입력으로 주어진다.
#
# 해당 날짜의 유효성을 판단한 후, 날짜가 유효하다면
#
# [그림1] 과 같이 ”YYYY/MM/DD”형식으로 출력하고,
#
# 날짜가 유효하지 않을 경우, -1 을 출력하는 프로그램을 작성하라.
#
#
# 연월일로 구성된 입력에서 월은 1~12 사이 값을 가져야 하며
#
# 일은 [표1] 과 같이, 1일 ~ 각각의 달에 해당하는 날짜까지의 값을 가질 수 있다.
#
# ※ 2월의 경우, 28일인 경우만 고려한다. (윤년은 고려하지 않는다.)




a = int(input())
k = []
year = []
month = []
day = []



D_31 = ['01', '03', '05', '07', '08', '10', '12']
D_30 = ['04', '06', '09', '11']
D_28 = ['02']
# 8개 짜리 스트링 받아오면 4개 ,2개 ,2개 순으로 짜르고
# 가운데 2개 우선 13보다 작은지 판별하고
# in 써서 저기에 들어가고 31보다 크면 false 조건문 여러개

for i in range(a):
    b = list(map(str, input()))
    year = ''.join(b[:4])
    month = ''.join(b[4:6])
    day =''.join(b[6:8])
    if month in D_31:
        if int(day) < 32:
            print('#{} {}/{}/{}'.format(i+1, year, month, day))
        else:
            print('#{} -1'.format(i+1))
    elif month in D_30:
        if int(day) < 31:
            print('#{} {}/{}/{}'.format(i+1, year, month, day))
        else:
            print('#{} -1'.format(i+1))
    elif month in D_28:
        if int(day) < 29:
            print('#{} {}/{}/{}'.format(i+1, year, month, day))
        else:
            print('#{} -1'.format(i+1))
    else:
        print('#{} -1'.format(i+1))


