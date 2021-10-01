
import sys

t = int(sys.stdin.readline())
number_dict = {i : 0 for i in range(1,10001) }
for _ in range(t):
    N = int(sys.stdin.readline())
    number_dict[N] += 1

for key,value in number_dict.items():

    if value != 0:

        for __ in range(value):

            print(key)
