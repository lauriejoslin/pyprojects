x = []
test = []
def partition(array):
    if len(array) == 0:
        return array
    if len(array) ==1:
        return array
    if len(array) ==2:
        if array[0] < array[1]:
            return array[0], array[1]
        else:
            low = array[0]
            array[0] = array[1]
            array[1] = low
            return array[0], array[1]
    if len(array) >2:
        n = 0
        k = 0
        pivot = array[-1]
        low = array[n]
        high = array[-2-k]
        while low != high:
            if low > pivot:
                while high >= pivot and k < len(array) -n:
                    if low == high:
                        break
                    k +=1
                    high = array[-2-k]

                if high < pivot:
                    
                    array[n] = high
                    array[-2-k] = low
                    if k <= len(array) and n <= len(array):
                        n +=1
                        k +=1
                        low = array[n]
                        high = array[-2-k]

            elif low < pivot:
                
                n +=1
                low = array[n]
                
        array[-1] = low
        array[n] = pivot
        part1 = array[:n]
        part2 = array[n+1:]
        a = part1    
        b = part2 
        if len(a) <3 and len(a) >0:
            if len(a) ==2:
                x.append(a[0])
                x.append(a[1])
                x.append(pivot)
            else:
                x.append(a)
                x.append(pivot)
        if len(b) <3 and len(b) >0:
            if len(b) ==2:
                x.append(pivot)
                x.append(b[0])
                x.append(b[1])
            else:
                x.append(pivot)
                x.append(b)
        partition(part1)
        partition(part2)
        return None


test = [1, 3, 7, 33, 9, 8, 5, 2]
partition(test)
print(x)


            


