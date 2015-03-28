import mydeque

def palindrome_check(word) :
    deque = mydeque.Deque()
    for letter in word :
        deque.add_front(letter)

    char_equal = True

    while deque.size() > 1 and char_equal :
        first = deque.remove_front()
        last = deque.remove_rear()

        if first != last :
            char_equal = False

    return char_equal


print palindrome_check("radar")
print palindrome_check("qwertyuiop")
