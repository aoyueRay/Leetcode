#-*- coding:utf-8 -*-

"""
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.
"""

# Runtime = 60ms
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        count = 1
        string = "1"
        while(count < n):
            string = self.countNext(string)    # 递归获取下一个字符串
            count += 1
        return(string)

    # 获取下一个字符串
    def countNext(self,string):
        length = len(string)
        num = string[0]    # 用于对比的元素
        count = 1
        output = ""
        for t in range(1,length):
            if string[t - 1] == string[t]:    # 前后相同的情况
                num = string[t]
                count += 1
            else:    # 前后不同的情况
                output = output + str(count) + num    # 根据统计，生成部分字符串
                num = string[t]    # 变更对比元素
                count = 1    # 重置统计数
        output = output + str(count) + num
        return(output)


# 根据规则，每次递归的生成下一组字符串
# Runtime = 60ms
class Solution_1(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        number = 1
        next_str = '1'    # 定义初始字符串
        count_list = ['1']
        while number < n:
            next_str = self.generate_next(next_str)    # 递归产生下一个字符串
            count_list.append(next_str)
            number += 1
        print(count_list)
        return(next_str)

    # 根据输入的字符串以及生成规则，产生下一个字符串
    # 输入：string字符串
    # 输出：nest_str字符串
    def generate_next(self,string):
        next_str = ''
        init_index = 0    # 初始化基础指针
        move_index = 1    # 初始化移动指针
        count = 1    # 初始化个数
        comp_str = string[0]
        while move_index < len(string):
            if string[move_index] == comp_str:    # 下一个元素与当前指向的元素相同
                count += 1
                move_index += 1
            else:
                temp_str = str(count) + comp_str    # 根据规则组成字符串
                next_str += temp_str
                count = 1    # 重置计数
                comp_str = string[move_index]    # 重置对比元素
                move_index += 1
        temp_str = str(count) + comp_str    # 处理最后一段元素
        next_str += temp_str
        return(next_str)


if __name__ == '__main__':
    solution = Solution()
    n = 1
    ans = solution.countAndSay(n)
    print(ans)
