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
    for i in range(1, arrlen):
        lo = arr[nlo]
        hi = arr[nhi]
        if nlo == nhi:
            break
        if lo > pivot:
            while hi >= pivot:
                nhi -= 1
                hi = arr[nhi]
            if hi < pivot:
                arr[nlo] = hi
                arr[nhi] = lo
        elif lo < pivot:
            nlo +=1
    lo = arr[nlo]
    arr[-1] = lo
    arr[nlo] = pivot
    part1 = arr[:nlo]
    part2 = arr[nlo]
    part3 = arr[nlo +1:]
    return quicksort(part1), quicksort(part2), quicksort(part3)

test = [1, 5, 2, 7, 4, 3]
quicksort(test)
print(sorted)



    