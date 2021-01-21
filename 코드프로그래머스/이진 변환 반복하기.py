def solution(s):
    answer = []
    zero_list= []
    convert_list = []
    def convert(number):
        print(number)
        number_length = len(number)
        convert_number = []

        while number_length != 0:
            print(number_length)
            if number_length % 2 == 0:
                convert_number.append('0')
            elif number_length % 2 == 1:
                convert_number.append('1')

            number_length = number_length // 2


        print(convert_number)
        a = ''.join(convert_number)[::-1]
        convert_list.append(1)

        if a == '1':
            return
        else:
            delete_zero(a)


    def delete_zero(number):
        convert_number = ''
        for i in number:
            if int(i) == 0:
                zero_list.append(0)
            elif int(i) == 1:
                convert_number = convert_number + i
        convert(convert_number)




    delete_zero(s)
    print(len(convert_list))
    print(len(zero_list))

    return [len(convert_list), len(zero_list)]

s = "110010101001"
solution(s)