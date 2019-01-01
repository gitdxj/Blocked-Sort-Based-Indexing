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

    dic.add("word")
    dic.add("new")
    dic.add("hello world")
    dic.add("new")
    dic.write2file("index.txt")
    dic.print_dic()

