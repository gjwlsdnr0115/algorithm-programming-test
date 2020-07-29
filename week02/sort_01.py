def solution(array, commands):
    answer = []
    for cmd in commands:
        cut = array[cmd[0]-1:cmd[1]]
        sort_cut = quick_sort(cut)
        answer.append(sort_cut[cmd[2]-1])
    return answer

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

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))