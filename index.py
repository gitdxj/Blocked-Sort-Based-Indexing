import csv
import os
import split


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
    name = '/home/fr/Desktop/test.csv'
    a = get_index(name)