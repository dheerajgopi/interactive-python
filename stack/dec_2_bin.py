import mystack

def dec_2_bin(n) :
    stack = mystack.Stack()

    while n > 0 :
        stack.push(n % 2)
        n /= 2

    bin_string = ""

    while not stack.is_empty() :
        bin_string += str(stack.pop())

    return bin_string

print dec_2_bin(8)
