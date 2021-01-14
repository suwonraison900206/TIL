#-*- coding:utf-8 -*-
import sys
import collections

QUESTION_IS = "문자열 S와 T를 입력받아 O(n) 에 T의 모든 문자가 포함된 S의 최소 윈도우를 찾아라"


def solution(search, target):
    print(search, target)
    need = collections.Counter(target)
    missing = len(target)
    left = start = end = 0
    print(need)
    print(need)
    for right, char in enumerate(search, 1):
        missing -= need[char] > 0
        need[char] -= 1

        if missing == 0:
            while left < right and need[search[left]] < 0:
                need[search[left]] += 1
                left += 1

            if not end or right - left <= end - start:
                start, end = left, right

                need[search[left]] += 1
                missing += 1
                left += 1


    return search[start:end]


S = "ADOBECODEBANC"
T = "ABC"

solution(S, T)