#-*- coding:utf-8 -*-

"""
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

"""

# 初始化一个索引指向第一个字符。
# 从第一个字符开始，依次替换为对应的字母，生成一个临时的变量列表，保存替换后的字符串
# 将临时列表拷贝给返回列表，索引后移，替换下一个字符。知道最后一位被替换完成。
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return([])    # 字符串为空时，返回空列表
        letter = {}    # 定义字典保存数字与字母的对应关系
        letter['1'] = ''
        letter['2'] = 'abc'
        letter['3'] = 'def'
        letter['4'] = 'ghi'
        letter['5'] = 'jkl'
        letter['6'] = 'mno'
        letter['7'] = 'pqrs'
        letter['8'] = 'tuv'
        letter['9'] = 'wxyz'
        letter['0'] = ''

        begin = 0    # 初始化指针指向当前处理的数字
        temp_list = []    # 初始化列表，用于保存临数的变量
        answer = [digits]    # 初始化列表，用于保存最终的返回值
        while begin < len(digits):
            each_digit = letter[digits[begin]]  # 根据数字找到对应的字母
            for each_letter in each_digit:
                for each_str in answer:
                    temp_str = each_str.replace(each_str[begin],each_letter,1)    # 将数字替换为字母，每次替换一个数字字符
                    temp_list.append(temp_str)
            answer = temp_list[:]    # 将临时变量列表拷贝给最终列表
            temp_list = []    # 将临时变量列表清空
            begin += 1
            print('answer -> ',answer)
        return(answer)


if __name__ == '__main__':
    solution = Solution()
    digits = '232'
    ans = solution.letterCombinations(digits)
    print(ans)