def mergesort(alist) : #sorts inplace
    if len(alist) > 1 :
        mid = len(alist) / 2
        left = alist[:mid]
        right = alist[mid:]

        mergesort(left)
        mergesort(right)
        
        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right) :
            if left[i] < right[j] :
                alist[k] = left[i]
                i += 1
            else :
                alist[k] = right[j]
                j += 1
            k += 1

        while i < len(left) :
            alist[k] = left[i]
            i += 1
            k += 1

        while j < len(right) :
            alist[k] = right[j]
            j += 1
            k += 1


a = [7,2,5,9,10,1,3,6,4]
print a
mergesort(a)
print a
