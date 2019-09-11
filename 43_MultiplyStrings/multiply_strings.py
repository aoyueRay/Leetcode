#-*- coding:utf-8 -*-

"""
Given two numbers represented as strings, return multiplication of the numbers as a string.

Note:

    The numbers can be arbitrarily large and are non-negative.
    Converting the input string to integer is NOT allowed.
    You should NOT use internal library such as BigInteger.

"""

# 通过ord()函数，将字符转换为数字
# Runtime = 80ms
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num_1 = self.change_to_int(num1)
        num_2 = self.change_to_int(num2)
        return(str(num_1 * num_2))



    # 将字符串转换为数字
    # ord()将字符转化为ascii码
    # 输入：字符串string
    # 输出：数字num
    def change_to_int(self,string):
        length = len(string)
        index = 0
        num = 0
        while index < length:
            each_str = string[index]
            each_num = ord(each_str)  - ord('0')
            num = num * 10 + each_num
            index += 1
        return(num)


if __name__ == '__main__':
    solotion = Solution()
    num1 = '11'
    num2 = '11'
    ans = solotion.multiply(num1,num2)
    print(ans)