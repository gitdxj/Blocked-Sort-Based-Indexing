import infix2postfix
import index
import calculate
import dictionary


def outcome_list(expression, inverted_index):  # 根据表达式和倒排索引表产生结果list
    postfix_list = infix2postfix.infix2postfix(expression)
    outcome = calculate.cal(postfix_list, inverted_index)
    return outcome


if __name__ == '__main__':
    index = index.read_index_file()
    dic = dictionary.Dictionary()
    dic.read_file(index)
    # print(dex)
    e = "Frank AND guy"
    post = infix2postfix.infix2postfix(e)
    print(post)
    print(dic.get_position("Frank"))
    print(index['59'])
    print(dic.get_position("guy"))
    print(index['107'])
    outcome = outcome_list(e, index)
    print(outcome)
