import csv
import os
import split
from dictionary import Dictionary
import language


# 创建倒排索引,返回倒排索引表
def create_index(file_name):
    csv_file = open(file_name)
    csv_reader = csv.reader(csv_file)
    row_num = 0
    inverted_index = {}
    for row in csv_reader:
        row_num = row_num + 1
        for string in row:
            if ' ' in string:
                word_list = split.split_word(string)
                for word in word_list:
                    if word not in inverted_index:
                        inverted_index[word] = [row_num]
                    elif row_num not in inverted_index[word]:
                        inverted_index[word].append(row_num)
            else:
                if string not in inverted_index:
                    inverted_index[string] = [row_num]
                elif row_num not in inverted_index[string]:
                    inverted_index[string].append(row_num)
    return inverted_index


# assignment#4的创建倒排索引的函数, ex表示extended
def create_index_ex(file_name):
    dic = Dictionary()
    csv_file = open(file_name)
    csv_reader = csv.reader(csv_file)
    rows = [row for row in csv_reader]  # csv表格中每一行都在rows中了
    # 每一个row结束之后进行merge
    for row_no in range(len(rows)):
        index = []  # 倒排索引表是一个列表
        row = rows[row_no]  # row是csv表格中的一行
        for string in row:  # string是csv表格中的一项
            words = language.text_process(string)
            words = language.get_dictionary_list(words)  # 完成分词
            # 把csv表格中一项的所有词项写入词典，并建立索引表
            for word in words:
                dic.add(word)
                word_ptr = dic.get_position(word)
                if word_ptr not in index:  # 若倒排索引表中没有这个词项
                    index.append(word_ptr)
        index = sorted(index)
        # 把index里面的term_ptr转为字符串，这一步是为了后面的join
        for i in range(len(index)):
            index[i] = str(index[i])
        # 读完每一行就创建一个文件来保存这一行中出现的term指针
        f_name = str(row_no) + '.txt'
        f_name = 'index/' + f_name
        f = open(f_name, 'w')
        doc_content = ','.join(index)
        # 指针列表也不会太大，我到时候直接读一个文件进来也不过分
        f.write(doc_content)
        f.close()
        # print(index)
    dic.write2file('dictionary.txt')
    return index


# 把create_index_ex中得到的好多好多个文件都merge起来，合成一个大倒排索引表.txt
def merge(doc_num):
    filename = 'inverted_index.txt'
    f = open(filename, 'w')
    f.close()
    ''' 
    打开一个之前建立好的一个文档的索引文件，例如0.txt，其中记录了docID为0的文档中词项的集合
    读入，得到doc_term_list
    然后打开总的倒排记录表文件，按行读取，把读到的词项都加到index_term_list中
    对于doc_term_list和index_term_list中都有的词项，把docID加到相应倒排记录上
    对于doc_term_list中有而index_term_list中没有的词项，创建新的倒排记录项
    '''
    for doc_no in range(doc_num):
        doc_name = 'index/' + str(doc_no) + '.txt'
        doc_file = open(doc_name, 'r')
        doc_term_list = doc_file.read().split(',')  # term_list是doc_no文档中的词项集合
        index_term_list = []  # 用来记录当前倒排索引表中的所有词项
        index_file = open(filename, 'r')
        data = []
        while True:
            line = index_file.readline()
            if not line:
                break
            find_semicolon = line.find(':')
            index_term = line[0:find_semicolon]
            index_term_list.append(index_term)
            if index_term in doc_term_list:  # 如果这个词项在doc_no中出现过，则把doc_no加在倒排记录表上
                line = line.strip('\n')  # 去掉尾部的\n
                line = line + ',' + str(doc_no) + '\n'
            data.append(line)
        index_file.close()
        for doc_term in doc_term_list:
            if doc_term not in index_term_list:
                new_line = str(doc_term) + ':' + str(doc_no) + '\n'
                data.append(new_line)
        index_file = open(filename, 'w')
        index_file.writelines(data)


def read_index_file():
    index = {}
    if not os.path.isfile('inverted_index.txt'):
        return index
    file = open('inverted_index.txt', 'r')
    while True:
        line = file.readline()
        if not line:
            break
        find_semicolon = line.find(':')
        index_term = line[0:find_semicolon]
        posting_list = line[find_semicolon+1:].strip('\n').split(',')
        if index_term not in index:
            index[index_term] = posting_list
    return index


# 为创建的倒排索引表文件命名
def rename(file_name):
    pre_name = ''
    for letter in file_name:
        if letter != '.':
            pre_name += letter
        else:
            break
    return pre_name + '_index.txt'


# 创建倒排索引文件
def create_index_txt(file_name):
    index = create_index(file_name)
    new_name = rename(file_name)
    index_file = open(new_name, 'w')
    index_file.write(str(index))


# 读取倒排索引文件
def read_index_txt(file_name):
    new_name = rename(file_name)
    index_file = open(new_name, 'r')
    inverted_index = eval(index_file.read())
    return inverted_index


def get_index(filename):
    new_file_name = rename(filename)
    if os.path.isfile(new_file_name):  # 若已经有倒排索引表了
        fr = open(new_file_name, 'r')  # 读取倒排索引表
        inverted_index = eval(fr.read())
        fr.close()
    else:                                                  # 若还没有倒排索引表
        inverted_index = create_index(filename)       # 创建新的倒排索引表
        fw = open(new_file_name, 'w')                      # 写入和要查找的文件相同的目录下
        fw.write(str(inverted_index))
        fw.close()
    return inverted_index


if __name__ == '__main__':
    index = read_index_file()
    dic = Dictionary()
    dic.read_file(index)
    dic.print_dic()
