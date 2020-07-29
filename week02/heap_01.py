import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)  # make scoville a heap priority queue
    while scoville[0] < K:  # food under K exists

        if len(scoville) == 1:  # can't mix any more foods
            return -1

        # mix two lead spicy foods
        f1 = heapq.heappop(scoville)
        f2 = heapq.heappop(scoville)
        mixed = f1 + 2 * f2
        heapq.heappush(scoville, mixed)

        answer += 1
    return answer

print(solution([1, 2, 3, 9, 10, 12], 7))