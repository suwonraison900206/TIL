
count = 0




def back(number):
    global count

    if len(number) == 1:
        if int(number[0]) % 2 == 0:
            return
        else:
            count += 1
            return

    elif len(number) == 2:
        new_number = 0

        for i in number:
            new_number += int(i)
        new = list(str(new_number))

        for i in new:
            if int(i) % 2 == 0:
                pass
            else:
                count += 1

        back(new)

    else:

N = list(input())
back(N)

