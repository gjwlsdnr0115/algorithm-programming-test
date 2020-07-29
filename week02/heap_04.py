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

def solution(operations):
    answer = []
    pq = []
    for op in operations:
        ops = op.split()
        if ops[0] == 'I':
            num = int(ops[1])
            pq.append(num)
            pq = quick_sort(pq)
        else:
            if len(pq) != 0:
                if ops[1] == '1':
                    pq.pop()
                else:
                    pq.pop(0)
    if len(pq) == 0:
        answer = [0, 0]
    else:
        answer.append(pq[len(pq) - 1])
        answer.append(pq[0])

    return answer