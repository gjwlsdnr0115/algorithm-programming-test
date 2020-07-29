import heapq

def solution1(jobs):
    total_jobs = len(jobs)
    heap = []
    for job in jobs:
        length = job[1]-job[0]-1
        heap.append(length)

    heapq.heapify(heap)

    total_time = 0

    while len(heap) > 0:
        next = heapq.heappop(heap)
        total_time += len(heap) * next

    answer = total_time / total_jobs
    return answer

def solution2(jobs):
    running = False
    total_jobs = len(jobs)
    current_job = 0
    heap = []
    current_time = 0
    jobs.reverse()
    wait_time = 0

    while True:
        if len(jobs) > 0 and jobs[len(jobs)-1][0] == current_time:
            next = jobs.pop()
            length = next[1] - next[0] - 1
            heapq.heappush(heap, length)

        if not running and len(heap) > 0:
            run = heapq.heappop(heap)
            current_job = run
            running = True

        if running:
            current_job -= 1
            wait_time += len(heap) + 1
            if current_job == 0:
                running = False
        else:
            wait_time += len(heap)

        current_time += 1

        if not running and len(heap) == 0 and len(jobs) == 0:
            break

    answer = wait_time / total_jobs
    return answer

def solution(jobs):
    total_jobs = len(jobs)
    jobs_sorted = sorted(jobs, key=lambda x: x[0], reverse=True)
    now = 0
    total_time = 0
    rq = []
    finished_jobs = 0

    while finished_jobs < total_jobs:
        while len(jobs_sorted) > 0 and now >= jobs_sorted[len(jobs_sorted)-1][0]:
            next = jobs_sorted.pop()
            length = next[1]
            heapq.heappush(rq, length)
        if len(rq) == 0:
            now += 1
        else:
            run = heapq.heappop(rq)
            total_time += (len(rq)+1) * run
            now += run
            for i in range(len(jobs_sorted)-1, -1, -1):
                if jobs_sorted[i][0] < now:
                    total_time += now - jobs_sorted[i][0]
                else:
                     break
            finished_jobs += 1

    return int(total_time / total_jobs)

print(solution([[0, 10], [2, 3], [9, 3]]))

