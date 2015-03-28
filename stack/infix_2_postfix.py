import mystack

def infix_2_postfix(infix_exp) :
    precedence = {}
    precedence["*"] = 3
    precedence["/"] = 3
    precedence["+"] = 2
    precedence["-"] = 2
    precedence["("] = 1

    opstack = mystack.Stack()
    postfix_list = []
    token_list = infix_exp.split()

    for token in token_list :
        if token in "0123456789" or token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" :
            postfix_list.append(token)
        elif token == "(" :
            opstack.push(token)
        elif token == ")" :
            top_token = opstack.pop()
            while top_token != "(" :
                postfix_list.append(top_token)
                top_token = opstack.pop()
