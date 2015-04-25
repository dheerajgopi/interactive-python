def quicksort(alist) :
    quicksort_helper(alist, 0, len(alist) - 1)

def quicksort_helper(alist, first, last) :
    if first < last :
        splitPoint = partition(alist, first, last)

        quicksort_helper(alist, first, splitPoint - 1)
        quicksort_helper(alist, splitPoint + 1, last)

def partition(alist, first, last) : #pivot reaches its correct position in this func
    pivotValue = alist[first] #first term as pivot
    left = first + 1
    right = last
    done = False

    while not done : #moving left and right markers until they pass each other
        while left <= right and alist[left] <= pivotValue :
            left += 1

        while right >= left and alist[right] >= pivotValue :
            right -= 1

        if right < left :
            done = True
        else :
            alist[left], alist[right] = alist[right], alist[left] #exchanging left & right val

    alist[first], alist[right] = alist[right], alist[first] #exchanging first term & right val
    return right

a = [5,9,1,5,2,8,3,10]
print a
quicksort(a)
print a
