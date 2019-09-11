# -*- coding:utf-8 -*-

"""
 You are given a string, s, and a list of words, words, that are all of the same length.

 Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

For example, given:
s: "barfoothefoobarman"
words: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).
"""

# Solution_2的改进，统计每个words元素出现的个数，构造成一个字典
# 再按杖元素长度依次截取s，并看截取的字符串是否在words中，存在的话对应的个数减一。
# 直到所有的个数为0时，即为索引值。
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        answer = []  # 返回列表
        if not words:
            return ([0])

        length = len(words[0])  # 获取每个子串的长度
        length_words = len(words)    # words的长度 ,length * length_words是拼接后子串的长度
        index_s = 0
        count_dict = {}
        # 利用for循环构造字典
        # 此处如果使用python的BIF，count_dict[each_word] = words.count(each_word)，则导致超时
        for each_word in words:
            if each_word in count_dict:
                count_dict[each_word] += 1
            else:
                count_dict[each_word] = 1
        while index_s <= len(s) - length * length_words:    # 截取一段字符串，长度与words中元素能拼接的最长字符串长度相等
            temp_index = index_s  # 初始化截取字符串的索引
            comp_str = s[temp_index:temp_index + length * length_words]  # 截取用于对比的字符串
            flag = self.judge_substring(comp_str,length,count_dict)
            if flag:
                answer.append(index_s)
            index_s += 1  # s的索引加length
        return(answer)

    # 判断截取的字符串与words中的串是否匹配
    # 输入：截取的字符串comp_str，length，用于对比的字典count_dict
    # 输出：判断结果True or False
    def judge_substring(self,comp_str,length,count_dict):
        temp_dict = count_dict.copy()    # 使用拷贝函数，避免原字典被修改
        init_index = 0
        while init_index <= len(comp_str) - length:
            word = comp_str[init_index:init_index + length]
            if (word in temp_dict) and temp_dict[word] != 0:    # 字符串在字典中存在，且个数不为0时，将个数减一
                temp_dict[word] -= 1
            else:
                return False
            init_index += length
        return True


# 依次从s上截取字符串，将截取的字符串与words中的元素比对，相等则删去words中的元素，并截取下一个字符串。
# 依次比对，若words中元素最后为空，则返回s的索引值。否则s的索引后移，并进行下一轮比对。
# 依旧超时。。。不可取
class Solution_2(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        print('*' * 20)
        print(s)
        answer = []  # 返回列表
        if not words:
            return([0])

        length = len(words[0])    # 获取每个子串的长度
        index_s = 0
        while index_s < len(s):
            temp_words = words[:]  # 拷贝一个words用于操作，每次循环后重置
            temp_index = index_s    # 初始化截取字符串的索引
            comp_str = s[temp_index:temp_index + length]    # 截取用于对比的字符串
            while (comp_str in temp_words):
                temp_words.remove(comp_str)    # 若words中存在该字符串，则删去
                temp_index += length
                comp_str = s[temp_index:temp_index + length]
            if not temp_words:    # words中所有的元素都匹配上了
                answer.append(index_s)
            index_s += 1    # s的索引加一
        return(answer)



# 即无序连接words中的字符串，并在s中查找字符串是否存在，若存在则返回起始位置的索引
# 先找到所有可能的子串
# 再通过每个子串一一去比对原串，找到所在的索引位置
# 超时，不可取
class Solution_1(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        print('*' * 20)
        print(s)
        if not words:
            return([0])
        answer = []    # 初始化返回列表
        index = 0    # 初始化索引
        sub_string = self.get_substring(words)    # 获取所有可能子串的列表
        print('*' * 20)
        print(sub_string)
        print('*' * 20)
        for each_sub in sub_string:
            length = len(each_sub)    # 获取子串的长度
            index = 0
            while index < len(s):
                comp_str = s[index:index + length]    # 截取用于对比的字符串
                if comp_str == each_sub:
                    answer.append(index)
                index += 1
        return(answer)

    # 定义一个函数，输入列表，返回该列表中所有元素可能组合成的子串的集合列表
    # 输入：words: List[str]，words长度不为空
    # 输出：sub_string: List[str]，words中所有元素拼接所得的，所有可能的长串的列表集合
    def get_substring(self,words):
        init_index = 0    # 定义索引指针，指向元素拼接的位置
        temp_index = 0
        sub_string = []    # 返回值列表
        temp_string = []    # 定义临时列表，其中每个元素也都是列表
        temp_string.append(words[:1])    # 初始化为words的第一个元素
        temp_sub_string = []    # 临时变量，保存中间结果
        for each_index in range(1,len(words)):
            each_word = words[each_index:each_index + 1]
            for each_temp in temp_string:
                while init_index < len(each_temp) + 1:
                    each_list = each_temp[:init_index] + each_word + each_temp[init_index:]    # 拼接
                    temp_sub_string.append(each_list)
                    init_index += 1
                init_index = 0    # 重置索引指针
            temp_string = temp_sub_string[:]  # 重置用于处理的列表
            temp_sub_string = []    # 重置临时列表

        for i in temp_string:
            sub_str = ''.join(i)    # 转换为字符串
            if sub_str not in sub_string:
                sub_string.append(sub_str)    # 去重
        return(sub_string)



if __name__ == '__main__':
    solution = Solution()
    s = 'barfoofoobarthefoobarman'
    words = ["bar","foo","the"]
    s = "wordgoodgoodgoodbestword"
    words = ["word", "good", "best", "good"]
    s = "lingmindraboofooowingdingbarrwingmonkeypoundcake"
    words = ["fooo", "barr", "wing", "ding", "wing"]

    ans = solution.findSubstring(s,words)
    print(ans)