


def fibo(number):
    print(number)
    if number == 1 or number == 2:
        return 1
    else:

        return fibo(number-2) + fibo(number-1)





N = int(input())
print(N)

fibo(N)