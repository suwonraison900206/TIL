# i = 0
# while i < 5:
#     print('num : ',i)
#     i+=1

# dan = int(input())
# i = 0
# while i <=9:
#     print('{} * {} = {}'.format(dan,i,dan*i))
#     i+=1

#for문
#조건보다 횟수에 비중을 둘 때 사용하는 반복문
#시작값,종료값,증감을 한문장에 씀
#조건이 참인 동안 실행

#0부터 10까지의 합을 구하세요
# sum = 0
# for i in range(0,10+1):
#     # print(i)
#     sum += i
# print(sum)

#5부터 10까지의 합은?
# sum = 0
# for i in range(5,10+1):
#     # print(i)
#     sum += i
# print(sum)

#0부터 10까지의 짝수의 합
# sum = 0
# for i in range(5,10+1,2):
#     # print(i)
#     sum += i
# print(sum)
#이 문장을 이용해서 아래와같이 출력하기
# for i in range(1):
#     print('*',end='')
# print()
# for i in range(2):
#     print('*',end='')
# print()
# for i in range(3):
#     print('*',end='')
# print()
for j in range(5+1):
    for i in range(j):
        print('*',end='')
    print()

'''
*
**
***
****
*****
'''











