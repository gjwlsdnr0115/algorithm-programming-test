def heap_sort(a):
    size = len(a)
    for i in range(size // 2 - 1, -1, -1):
        downheap(a, i, size)

    for i in range(size -1, 0, -1):
        a[0], a[i] = a[i], a[0]
        downheap(a, 0, i)

    return a

def downheap(a, idx, size):
    max_idx = idx
    left_index = 2 * idx + 1
    right_index = 2 * idx + 2
    if left_index < size and a[left_index] > a[max_idx]:
        max_idx = left_index
    if right_index < size and a[right_index] > a[max_idx]:
        max_idx = right_index
    if max_idx != idx:
        a[max_idx], a[idx] = a[idx], a[max_idx]
        downheap(a, max_idx, size)

if __name__ == '__main__':
    test = [3, 8, 33, 9, 1, 5, 9, 10, 2]
    print(f'Original array: {test}')
    print(f'Sorted array: {heap_sort(test)}')
