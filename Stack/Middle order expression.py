from pythonds.basic import Stack
import string

def infixToPostfix(infixexpr):
    #记录操作符优先级
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1

    opStack = Stack()             #保存运算符
    postfixList = []              #保存结果
    tokenList = infixexpr.split() #解析表达式到单词列表

    for token in tokenList:
        if token in string.ascii_uppercase: #操作数
            postfixList.append(token)
        elif token == "(":
            opStack.push(token)
        elif token == ")":
            topToken = opStack.pop()
            while topToken != "(":
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:                                #操作符
            while (not opStack.isEmpty()) and \
                    (prec[opStack.peek()] >= prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop()) #操作符

    return " ".join(postfixList)           #合成后缀表达式字符串

print(infixToPostfix("( A + B ) * C"))