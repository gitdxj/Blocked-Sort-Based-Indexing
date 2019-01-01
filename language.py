import nltk
from nltk.stem import WordNetLemmatizer

english_punctuations = [',', '.', ':', ';', '?', '(', ')', '[', ']', '&', '!', '*', '@', '#', '$', '%']


def text_process(text):
    sens = nltk.sent_tokenize(text)  # 首先对文本进行分句
    words = []
    for sent in sens:
        word_in_sent = nltk.word_tokenize(sent)  # 对句子进行分词
        words += word_in_sent
    lemmatizer = WordNetLemmatizer()
    words = [word for word in words if word not in english_punctuations]  # 去除标点符号
    for i in range(len(words)):
        words[i] = lemmatizer.lemmatize(words[i])  # 词性还原
    return words


def get_dictionary_list(word_list):  # 扩充词典，增加二元短语
    new_list = [word for word in word_list]
    for i in range(len(word_list) - 1):
        phrase = word_list[i] + ' ' + word_list[i+1]
        new_list.append(phrase)
    return new_list


if __name__ == '__main__':
    example_sent = "this is fucking good."
    words = text_process(example_sent)
    words = get_dictionary_list(words)
    print(words)