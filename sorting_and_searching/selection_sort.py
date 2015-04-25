def selection_sort(alist) : #variant of bubble sort
    for pass_num in xrange(len(alist) - 1, 0, -1) : #finds highest elem in each loop
        high_index = 0
        for i in xrange(1, pass_num + 1) : #next highest elem placed in pos for each loop
            if alist[i] > alist[high_index] :
                high_index = i
        alist[pass_num], alist[high_index] = alist[high_index], alist[pass_num]

a = [9,2,6,4,8,2]
print a
selection_sort(a)
print a
