def solution(phone_book):
    answer = True  # return value
    for i in range(len(phone_book)):
        prefix = phone_book[i]  # set prefix
        for j in range(len(phone_book)):
            num = phone_book[j]  # compare number
            if prefix == num[:len(prefix)] and i != j:  # has prefix and is not itself
                answer = False
                break  # break loop

        if answer == False:  # if prefix found
            break  # break loop

    return answer

l = ['119', '97674223', '1195524421']
l2 = ['123', '456', '789']
l3 = ['12', '123', '1235', '567', '88']
print(solution(l3))