import mystack

def base_converter(n, base) :
    digits = "0123456789ABCDEF"
    stack = mystack.Stack()

    while n > 0 :
        stack.push(n % base)
        n /= base

    bin_string = ""

    while not stack.is_empty() :
        bin_string += digits[stack.pop()]

    return bin_string

print base_converter(8, 2)
print base_converter(16, 8)
print base_converter(5040, 16)
