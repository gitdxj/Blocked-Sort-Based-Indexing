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
    new_list = []
    current_token = None
    for i in range(len(tokenList)):
        if tokenList[i] in operatorList or tokenList[i] in ['(', ')']:
            if not (current_token in operatorList or current_token in ['(', ')']):
                new_list.append(current_token)
            current_token = tokenList[i]
            new_list.append(current_token)
        # 若此词是一个普通单词，并且current_token也是一个普通单词或短语
        elif current_token not in operatorList and current_token not in ['(', ')']:
            if current_token is None:
                current_token = tokenList[i]
            else:
                current_token = current_token + ' ' + tokenList[i]
        # 此词是一个普通单词但，current_token是操作符或者括号
        else:
            current_token = tokenList[i]
    tokenList = []
    for phrase in new_list:
        '''
        把长度超过三个词的短语分成双词短语
        例如： Frank Underwood Claire
        分成： Frank Underwood AND Underwood Claire
        '''
        split_phrase = []
        if ' ' in phrase:
            split_phrase = phrase.split(' ')
        else:
            break
        if len(split_phrase) < 3:
            tokenList.append(phrase)
        else:
            tokenList.append('(')
            for i in range(len(split_phrase)-1):
                binary_phrase = split_phrase[i] + ' ' + split_phrase[i+1]
                tokenList.append(binary_phrase)
                if i != len(split_phrase) - 2:
                    tokenList.append('AND')
            tokenList.append(')')
    # print(tokenList)
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
    expr = 'Frank Underwood Claire AND ( M OR Lisa )'
    expr1 = 'Frank AND good'
    post = infix2postfix(expr)
    print(infix2postfix(expr1))

