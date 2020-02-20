def backtrack(a, k, input, s):
    #print(a,k)
    if s > 5:
        return

    if k == input:
        psum = 0
        for i in range(input):
            if a[i]:
                psum = psum + S[i]
        if psum == 10:
            for i in range(input):
                if a[i]:
                    print(S[i], end='')
            print()
    else:
        a[k] = 1
        backtrack(a, k + 1, input, s + a[k])
        a[k] = 0
        backtrack(a, k + 1, input, s)

a = [0] * 5
S = [1,2,3,4,5]

backtrack(a, 0,  5, 0)


#
# a =[0] * 4
# def backtrack(a, k, input):
#     #print(a,k)
#     if k == input:
#         print(a)
#     else:
#         k += 1
#         a[k] = 1
#         backtrack(a, k, input)
#         a[k] = 0
#         backtrack(a, k, input)
# backtrack(a, 0, 3)




