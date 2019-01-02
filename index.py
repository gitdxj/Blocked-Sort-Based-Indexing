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
        index = {}  # 倒排索引表是一个词典，key为指向词典string的指针，value为docID，在这里为行号
        row = rows[row_no]  # row是csv表格中的一行
        for string in row:  # string是csv表格中的一项
            words = language.text_process(string)
            words = language.get_dictionary_list(words)  # 完成分词
            # 把csv表格中一项的所有词项写入词典，并建立索引表
            for word in words:
                dic.add(word)
                word_ptr = dic.get_position(word)
                if word_ptr not in index:  # 若倒排索引表中没有这个词项
                    index[word_ptr] = []
                    index[word_ptr].append(row_no)
                else:  # 若倒排记录表中已经有了这个词项
                    diff = 0
                    for i in index[word_ptr]:
                        diff += i
                    diff = row_no - diff
                    if diff != 0:
                        index[word_ptr].append(diff)
    dic.write2file('dictionary.txt')
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
    name = 'test.csv'
    a = create_index_ex(name)
    print(a)