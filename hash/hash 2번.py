phone_book = [str(x) for x in input().split()]

phone_book = sorted(phone_book, key=lambda x : len(x))

for i in range(len(phone_book)) :
    for j in phone_book[i+1:] :
        if phone_book[i] in j  :
            ifphone_book[i][:len(phone_book[i])] == j[:len(phone_book[i])] :
                answer = False
                print(answer)
                print("Done!")

answer = True
print(answer)
