def swap(a, i, j):
    a[i], a[j] = a[j], a[i]
    return a

def bubble_sort(a):
    size = len(a)
    for i in range(size-1, 0, -1):
        for j in range(i):
            if a[j] > a[j+1]:
                #a = swap(a, j, j+1)
                a[j], a[j+1] = a[j+1], a[j]
    return a

if __name__ == '__main__':
    test = [3, 8, 33, 9, 1, 5, 9, 10, 2]
    print(f'Original array: {test}')
    print(f'Sorted array: {bubble_sort(test)}')
