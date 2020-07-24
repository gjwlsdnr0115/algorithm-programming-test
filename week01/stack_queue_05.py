def solution1(prices):
    answer = []

    for idx, stock in enumerate(prices):
        queue = prices[idx+1:]
        time = 0
        stop = False
        while not stop:
            if len(queue) == 0:
                stop = True
            else:
                next = queue.pop(0)
                if stock > next:
                    stop = True
                time += 1
        answer.append(time)
    return answer

def solution2(prices):
    answer = []
    for i in range(len(prices)):
        answer.append(len(prices)-1-i)
    for i in range(1, len(prices)):
        if prices[i-1] > prices[i]:
            for j in range(i):
                if prices[j] > prices[i] and answer[j] == len(prices)-1-j:
                    answer[j] = i-j
    return answer

def solution(prices):
    answer = [0]*len(prices)
    for i in range(len(prices)-1):
        for j in range(i+1, len(prices)):
            answer[i] += 1
            if prices[j] < prices[i]:
                break


    return answer

print(solution([1, 2, 3, 2, 3]))