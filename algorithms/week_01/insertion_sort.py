def insertion_sort(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

if __name__ == '__main__':
    test = [3, 8, 33, 9, 1, 5, 9, 10, 2]
    print(f'Original array: {test}')
    print(f'Sorted array: {insertion_sort(test)}')
