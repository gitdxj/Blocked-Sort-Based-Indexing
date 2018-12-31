import infix2postfix
import index
import calculate


def outcome_list(expression, inverted_index):  # 根据表达式和倒排索引表产生结果list
    postfix_list = infix2postfix.infix2postfix(expression)
    outcome = calculate.cal(postfix_list, inverted_index)
    return outcome

