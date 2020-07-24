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

if __name__ == '__main__':
    test = [3, 8, 33, 9, 1, 5, 9, 10, 2]
    print(f'Original array: {test}')
    print(f'Sorted array: {quick_sort(test)}')