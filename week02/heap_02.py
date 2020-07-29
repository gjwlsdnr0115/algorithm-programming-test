import heapq

def solution(stock, dates, supplies, k):
    answer = 0
    heap = []
    dates.reverse()
    supplies.reverse()

    end_idx = len(dates) - 1
    while stock < k:

        while len(dates) > 0 and dates[end_idx] <= stock:
            dates.pop()
            heapq.heappush(heap, -supplies.pop())
            end_idx -= 1

        stock -= heapq.heappop(heap)
        answer += 1

    return answer

print(solution(4, [4, 10, 15], [20, 5, 10], 30))