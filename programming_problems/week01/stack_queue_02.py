def solution(heights):
    answer = []
    for idx, tower in enumerate(heights):
        receive_towers = heights[:idx]  # list of towers in front
        found = False
        for i in range(idx):
            next = receive_towers.pop()  # pop nearest tower
            if next > tower:  # if tower can receive
                answer.append(idx-i)  # append tower num
                found = True
                break
        if not found:  # receivable tower not found
            answer.append(0)
    return answer

print(solution([6,9,5,7,4]))