arr1 = [17, 8, 3, 9, 11, 13, 16]


def insertion_sort(arr):
    # i, j
    for i in range(1, len(arr)):
        # range(1,len(arr)) means i is going from 1 to n
        j = i - 1
        key = arr[i]
        while j >= 0 and key < arr[j]:
            # shift
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = key
        print(arr)


insertion_sort(arr1)