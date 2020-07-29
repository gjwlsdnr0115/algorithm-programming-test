def partition(a, low, high):
    i = (low - 1)
    pivot = a[high]

    for j in range(low, high):

        if a[j] <= pivot:

            i = i + 1
            a[i], a[j] = a[j], a[i]

    a[i + 1], a[high] = a[high], a[i + 1]
    return (i + 1)

def sort(a, low, high):
    if low < high:
        pi = partition(a, low, high)

        a = sort(a, low, pi - 1)
        a = sort(a, pi + 1, high)

    return a

def quick_sort(a):
    sort(a, 0, len(a)-1)
    return a

def bigger_num(sorted_citations, i):
    count = 0
    idx = len(sorted_citations)-1
    while True:
        if i > sorted_citations[idx] or idx == -1:
            break
        else:
            count += 1
            idx -= 1
    return count

def solution(citations):
    answer = 0
    size = len(citations)
    sort_citations = quick_sort(citations)
    for i in range(sort_citations[size-1], -1, -1):
        if i <= bigger_num(sort_citations, i):
            answer = i
            break

    return answer

print(solution([3, 0, 6, 1, 5]))