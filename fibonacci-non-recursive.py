def fibonacci(n):
    arr = [0, 1]
    for i in range(1, n+1):
        arr.append(arr[i] + arr[i-1])
    return arr


print(fibonacci(75))
