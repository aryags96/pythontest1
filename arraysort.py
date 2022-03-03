def ordered_zeros(arr,l):
    arr.sort()
    count=0
    for i in range(l):
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1
    while count < l:
        arr[count] = 0
        count += 1
arr = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]
l = len(arr)
ordered_zeros(arr, l)
print(arr)