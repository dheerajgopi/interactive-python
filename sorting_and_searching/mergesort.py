def mergesort(alist) : #returns new sorted list
    if len(alist) < 2 :
        return alist
    mid = len(alist) / 2
    left = alist[:mid]
    right = alist[mid:]

    left_half = mergesort(left)
    right_half = mergesort(right)
        
    return merge(left_half, right_half)

def merge(left, right) :
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right) :
        if left[i] <= right[j] :
            result.append(left[i])
            i += 1
        else :
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result



a = [7,2,5,9,1,3,6,4]
print a
print mergesort(a)
