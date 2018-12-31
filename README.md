# Blocked-Sort-Based-Indexing
## 要求
1. 使用基于块的排序索引构建算法BSBI
2. 在前几个作业基础上支持短语查询
3. 实现词典和倒排索引表的压缩

## BSBI

## 短语查询
短语查询可以使用带位置信息的索引表或者简单的双词索引。
这次作业我们就水一水用双词索引吧！
### 双词索引
每两个连续的词组成词对（作为短语）来索引。
比如文本片段“Friend, Romans, Countrymen”会产生两个词对:
* friends romans
* romans countrymen
索引构建时将每个词对看成一个词项放入词典中。
查询时，将查询拆分成基于双词的布尔查询式。
例如：stanford university palo alto,处理方法：
stanford university **AND** university palo **AND** palo alto


## 词典压缩
我们把词典看成一个单一的字符串，词项用指向这个单一字符串某一位置的指针表示。

## 倒排记录表压缩
倒排记录表的压缩使用对间隔编码。
