import numpy as np
sorted = []

def quicksort(arr):
    if type(arr) == int:
        sorted.append(arr)
    if type(arr) == list:
        if len(arr) == 1:
            sorted.append(arr[0])
        elif len(arr) == 2:
            if arr[0]>arr[1]:
                sorted.append(arr[1])
                sorted.append(arr[0])
            else:
                sorted.append(arr[0])
                sorted.append(arr[1])
        else:
            partition(arr)

def partition(arr):
    arrlen = len(arr)
    nlo = 0
    nhi = arrlen -2
    pivot = arr[-1]
    while nlo != nhi:
        lo = arr[nlo]
        hi = arr[nhi]
        if lo > pivot:
            while hi > pivot and nlo != nhi:
                nhi -= 1
                hi = arr[nhi]
            if hi <= pivot:
                arr[nlo] = hi
                arr[nhi] = lo
        elif lo <= pivot:
            nlo +=1
    lo = arr[nlo]
    arr[-1] = lo
    arr[nlo] = pivot
    part1 = arr[:nlo]
    part2 = int(arr[nlo])
    part3 = arr[nlo +1:]
    if len(part1) == 0:
        return quicksort(part2), quicksort(part3)
    if len(part3) == 0:
        return quicksort(part1), quicksort(part2)
    return quicksort(part1), quicksort(part2), quicksort(part3)

test = list(np.random.randint(low = 1,high=100,size=10))
print(test)
quicksort(test)
print(sorted)



    