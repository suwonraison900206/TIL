def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(0, len(phone_book)-1):
        k = len(phone_book[i])
        print(k , phone_book[i])
        for j in range(i+1, len(phone_book)):
            if len(phone_book[j]) < k:
                pass
            else:
                print(phone_book[j][:k], phone_book[i])
                if phone_book[j][:k] == phone_book[i]:
                    return False


    return answer

phone_book = ["119", "97674223", "1195524421"]
solution(phone_book)