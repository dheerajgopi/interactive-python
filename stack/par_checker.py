import mystack

def par_checker(parString) :
    stack = mystack.Stack()
    balanced = True
    index = 0

    while index < len(parString) and balanced :
        symbol = parString[index]

        if symbol in "([{" :
            stack.push(symbol)
        else :
            if stack.is_empty() :
                balanced = False
            else :
                open_par = stack.pop()
                if not matches(open_par, symbol) :
                    balanced = False

        index += 1

    if balanced and stack.is_empty() :
        return True
    else :
        return False

def matches(opn, close) :
    opens = '([{'
    closes = ')]}'
    return opens.index(opn) == closes.index(close)

print par_checker("({()})")
print par_checker("(()}")
print par_checker("())")
