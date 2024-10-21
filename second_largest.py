def getSecondLargest(self, arr):
    # Code Here
    n = len(arr)
    if n == 0 or n == 1:
        return -1
    small = float("inf")
    second_small = float("inf")
    large = -1
    second_large = -1
    for i in range(n):
        small = min(small, arr[i])
        large = max(large, arr[i])
    for i in range(n):
        if arr[i] < second_small and arr[i] != small:
            second_small = arr[i]
        if arr[i] > second_large and arr[i] != large:
            second_large = arr[i]
    return second_large
