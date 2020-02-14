# A = []
#
# for i in range(3):
#     A.append(i)
#     print(A)
#
# print(A)
#
#
# for i in range(3):
#     A.pop()
#     print(A)
#
# print(A)
#
# A = '()()((()))'
# B = '((()((((()()((()())((()))))'
# i = []
# j = []
#
#
# for q in range(len(B)):
#     if B[q] == '(':
#         i.append(B[q])
#     elif B[q] == ')':
#         if len(i) != 0:
#             i.pop()
#         else:
#             print(False)
# if len(i) != 0:
#     print(False)
# else:
#     print(True)




def fibo(n):
    print("fibo(",n,") is called")
    if n<2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)


memo = [0,1]

def fibo1(n):
    print("fibo1(",n,") is called")
    if n >= 2 and len(memo) <= n:
        memo.append(fibo1(n-1) + fibo1(n-2))
    return memo[n]

def fibo2(n):
    f = [0, 1]

    print("fibo2(",n,") is called")
    for i in range(2, n + 1):
        f.append(f[i-1] + f[i-2])

    return f[n]
print("recursive fibo")
fibo(7)
print("recursivbe + memoization fibo")
fibo1(7)
print("dynamic fibo")
fibo2(7)











