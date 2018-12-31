from stack import *


def infix2postfix(infixexpr):  # 参数是中缀表达式
    prec = {}
    prec['NOT'] = 3
    prec['AND'] = 2
    prec['OR'] = 1
    prec['('] = 0
    operatorList = ['NOT', 'AND', 'OR']
    openStack = Stack()
    postficList = []
    tokenList = infixexpr.split()
    for token in tokenList:
        if token not in operatorList and token not in ['(', ')']:
            postficList.append(token)
        # 左括弧匹配
        elif token == '(':
            openStack.push(token)
        elif token == ')':
            toptoken = openStack.pop()
            # 非括弧符号匹配
            while toptoken != '(':
                postficList.append(toptoken)
                toptoken = openStack.pop()
        else:
            # 运算符优先级比较
            while (not openStack.empty()) and (prec[openStack.peek()] >= prec[token]):
                postficList.append(openStack.pop())
            openStack.push(token)
    while not openStack.empty():
        postficList.append(openStack.pop())
    return postficList


if __name__ == '__main__':
    expr = 'Frank AND ( M OR Lisa )'
    post = infix2postfix(expr)
    print(post)

