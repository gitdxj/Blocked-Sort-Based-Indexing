class Dictionary:
    '这是一个储存词项的类'
    __dic = {}  # 词典是一个词典
    __position = 0  # position 变量就是指向词典的指针

    def add(self, new_word):
        if new_word not in self.__dic:
            self.__dic[new_word] = self.__position
            self.__position += len(new_word)

    def print_dic(self):
        for each in self.__dic:
            print("word: " + each + "  position: " + str(self.__dic[each]))

    def write2file(self, filename):
        file = open(filename, "w")
        for each in self.__dic:
            file.write(each)
        file.close()

    def get_position(self, word):
        return self.__dic[word]

    def read_file(self, inverted_index):
        index = [i for i in inverted_index]
        file = open('dictionary.txt', 'r')
        string = file.read()
        file.close()
        for i in range(len(index)):
            ptr = int(index[i])
            if i + 1 < len(index):
                next_ptr = int(index[i+1])
                word = string[ptr:next_ptr]
                self.add(word)
            else:
                word = string[ptr:]
                self.add(word)

    # def readfile(self, filename):
    #     self.__dic = []  # 词典清空
    #     file = open(filename, "r")
    #     string = file.read()
    #     length = len(string)
    #     i = 0
    #     while i < length:
    #         word_len = int(string[i])
    #         word = string[i:i+word_len]
    #         new_entry = str(word_len) + word
    #         self.__dic.append(new_entry)
    #         i = i + word_len + 1


if __name__ == '__main__':

    dic = Dictionary()

    # dic.add("word")
    # dic.add("new")
    # dic.add("hello world")
    # dic.add("new")
    # dic.write2file("index.txt")
    # dic.print_dic()
    # string = 'hello,world'
    # print(string[2:4])
    dic.read_file()
    dic.print_dic()

