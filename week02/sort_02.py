def solution(numbers):
    answer = ''
    for i in range(len(numbers)):
        numbers[i] = str(numbers[i])
    sorted_nums = []
    for i in range(len(numbers)):
        temp = numbers[i] * 4
        sorted_nums.append((numbers[i], temp[:4]))
    sorted_nums.sort(key=lambda x: x[1], reverse=True)
    for num in sorted_nums:
        answer += num[0]
    if answer[0] == '0':
        return '0'

    return answer

print(solution([6, 10, 2]))