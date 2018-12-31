import op
import stack


def cal(postfix_list, inverted_index):  # 根据索引表对后缀表达式进行计算，返回结果列表
    cal_stack = stack.Stack()
    for word in postfix_list:
        if word not in ['NOT', 'AND', 'OR']:
            cal_stack.push(inverted_index[word])
        else:
            oprand2 = cal_stack.pop()
            oprand1 = cal_stack.pop()
            if word == 'NOT':
                temp_outcom = op.dif_op(oprand1, oprand2)
            elif word == 'AND':
                temp_outcom = op.and_op(oprand1, oprand2)
            elif word == 'OR':
                temp_outcom = op.or_op(oprand1, oprand2)
            cal_stack.push(temp_outcom)
    outcome = cal_stack.pop()
    return outcome

