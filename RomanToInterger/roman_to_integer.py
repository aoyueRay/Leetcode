#-*- coding:utf-8 -*-

"""
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
"""

# I-1
# V-5
# X-10
# L-50
# C-100
# D-500
# M-1000
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        output = 0    # 初始化一个返回值
        roman = ['I','V','X','L','C','D','M']
        level = [1,5,10,50,100,500,1000]
        priority = dict(zip(roman,level))    # 定义一个字段对应罗马字符与数字的对应关系

        pointer = 1    # 定义一个指针指向下一个字符
        for each in range(len(s)):
            if pointer == len(s):
                output = output + priority[s[each]]    # 党指针大于字符串最大索引长度时，加上最后一个字符对应的值，并跳出循环
                break
            if priority[s[each]] >= priority[s[pointer]]:    # 前一个值大于等于后一个值时，加上当前值
                output = output + priority[s[each]]
            else:
                output = output + priority[s[each]] * (-1)    # 前一个值小于后一个值时，减去当前值
            pointer += 1
        return(output)


if __name__ == '__main__':
    solution = Solution()
    str = 'DCXXI'
    # str = 'MDCLXVI'
    ans = solution.romanToInt(str)
    print(ans)