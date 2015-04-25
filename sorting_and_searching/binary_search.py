def binary_search(aList, item) :
    first = 0
    last = len(aList) - 1
    found = False

    while first <= last and not found :
        mid_point = (first + last) / 2
        if aList[mid_point] == item :
            found = True
        elif item < aList[mid_point] :
            last = mid_point - 1
        else :
            first = mid_point + 1

    return found


print binary_search([1,2,3,4,5,6,7,8,9], 7)
