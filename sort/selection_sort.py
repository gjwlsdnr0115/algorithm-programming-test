def swap(a, i, j):
    a[i], a[j] = a[j], a[i]
    return a

def selection_sort(a):
    size = len(a)
    for i in range(size):
        min = i
        for j in range(i+1, size):
            if a[j] < a[min]:
                min = j
        #a = swap(a, i, min)
        a[i], a[min] = a[min], a[i]
    return a

if __name__ == '__main__':
    test = [3, 8, 33, 9, 1, 5, 9, 10, 2]
    print(f'Original array: {test}')
    print(f'Sorted array: {selection_sort(test)}')
