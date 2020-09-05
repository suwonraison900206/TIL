# https://programmers.co.kr/learn/courses/30/lessons/60061
# -*- coding: utf-8 -*-


def solution(n, build_frame):
    # [x,y,a,b]
    # a = 0 기둥, 1 보
    # b = 0 삭제, 1 설치

    wall = [[0] * (n+1) for __ in range(n+1)]
    print(wall)
    # for i in range(len(wall)):
    #     print(wall[i])
    #
    #
    # print('---------------------')


    answer = [[]]
    return answer


n = 5
k = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]


solution(n, k)

# [x,y,a,b]
# a = 0 기둥, 1 보
# b = 0 삭제, 1 설치