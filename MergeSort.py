"""def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        merge(arr, left, right)


def merge(arr, left, right):
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i = i + 1
        else:
            arr[k] = right[j]
            j += 1

        k += 1

    while i < len(left):
        print('i ', i)
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        print('j ', j)
        arr[k] = right[j]
        j += 1
        k += 1


data = [17, 8, 3, 9, 11, 13, 21]
merge_sort(data)
print(data)
"""


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        print(left, right)
        merge_sort(left)
        merge_sort(right)
        merge(arr, left, right)


def merge(arr, left, right):
    i = j = k = 0
    # i will be used for left
    # j will be used for right
    # k will be used for arr

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


# data = [17, 8, 3, 9, 11, 13, 21]
data = [19, 26, 34, 23, 12, 2, 3, 45]
print(data)
merge_sort(data)
print(data)
