def solution(clothes):
    clothes_num = {}  # init dict
    for list_ in clothes:
        if list_[1] not in clothes_num.keys():  # if new kind
            clothes_num[list_[1]] = 1  # add key to dict
        else:
            clothes_num[list_[1]] += 1  # increse num of kind

    answer = 1  # init answer var
    for key in clothes_num.keys():
        answer *= (clothes_num[key] + 1)  # multiply possible combinations
    answer -= 1  # must wear at least one clothes
    return answer
