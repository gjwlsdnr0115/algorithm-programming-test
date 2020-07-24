def merge_sort(a):
    size = len(a)
    if size > 1:
        mid = size // 2
        left = a[:mid]
        right = a[mid:]

        left = merge_sort(left)
        right = merge_sort(right)

        return merge(left, right)
    return a

def merge(left, right):
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]
    return result

if __name__ == '__main__':
    test = [3, 8, 33, 9, 1, 5, 9, 10, 2]
    print(f'Original array: {test}')
    print(f'Sorted array: {merge_sort(test)}')
