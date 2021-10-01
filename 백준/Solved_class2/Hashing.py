L = int(input())
lst = list(input())

word_dict = {}
cnt = 1
for i in range(97 , 123):

    word_dict[chr(i)] = cnt
    cnt +=1

a = 0
for v, i in enumerate(lst):

    a = a + (word_dict[i] * (31 ** (v)))

print(a % 1234567891)
