def bubble_sort(alist) :
    for pass_num in xrange(len(alist) - 1, 0, -1) : #n-1 passes on list
        for i in xrange(0, pass_num) : #next highest terms are in place for each loop
            if alist[i] > alist[i + 1] : #swapping
                alist[i], alist[i + 1] = alist[i + 1], alist[i]

a = [9,2,5,7,3,4]
print a
bubble_sort(a)
print a
