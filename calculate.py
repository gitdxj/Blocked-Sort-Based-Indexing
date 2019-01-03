import op
import stack
from dictionary import Dictionary


# def cal(postfix_list, inverted_index):  # 根据索引表对后缀表达式进行计算，返回结果列表
#     cal_stack = stack.Stack()
#     for word in postfix_list:
#         if word not in ['NOT', 'AND', 'OR']:
#             cal_stack.push(inverted_index[word])
#         else:
#             oprand2 = cal_stack.pop()
#             oprand1 = cal_stack.pop()
#             if word == 'NOT':
#                 temp_outcom = op.dif_op(oprand1, oprand2)
#             elif word == 'AND':
#                 temp_outcom = op.and_op(oprand1, oprand2)
#             elif word == 'OR':
#                 temp_outcom = op.or_op(oprand1, oprand2)
#             cal_stack.push(temp_outcom)
#     outcome = cal_stack.pop()
#     return outcome


def cal(postfix_list, inverted_index):  # 根据索引表对后缀表达式进行计算，返回结果列表
    cal_stack = stack.Stack()
    dic = Dictionary()
    dic.read_file(inverted_index)
    for word in postfix_list:
        if word not in ['NOT', 'AND', 'OR']:
            cal_stack.push(inverted_index[str(dic.get_position(word))])
        else:
            oprand2 = cal_stack.pop()
            oprand1 = cal_stack.pop()
            if word == 'NOT':
                temp_outcome = op.dif_op(oprand1, oprand2)
            elif word == 'AND':
                temp_outcome = op.and_op(oprand1, oprand2)
            elif word == 'OR':
                temp_outcome = op.or_op(oprand1, oprand2)
            cal_stack.push(temp_outcome)
    outcome = cal_stack.pop()
    return outcome