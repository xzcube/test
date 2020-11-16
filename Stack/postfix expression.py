from pythonds.basic import Stack

def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenList = postfixExpr.split()
    for token in tokenList:
        if token in "0123456789":
            operandStack.push(eval(token))
        else:
            operand1 = operandStack.pop()
            operand2 = operandStack.pop()
            result = doMath(token, operand1, operand2)
            operandStack.push(result)
    return operandStack.pop()

def doMath(token, op1, op2):
    if token == "+":
        return op1 + op2
    elif token == "*":
        return op1 * op2
    elif token == "-":
        return op2 - op1
    else:
        return op2 / op1

print(postfixEval("5 4 /"))