
def solution(number, k):
    answer = ''

    result = [number[0]]
    number =list(number)
    flag = 0

    for i in range(1, len(number)):
        while k > 0 and result and result[-1] < number[i]:
            result.pop()
            k -= 1
        result.append(number[i])
        if k == 0:
            result = result + number[i+1:]
            break
    if k !=0:
        return ''.join(result[:-k])

    return ''.join(result)


number = '99999'
k = 2
solution(number, k)