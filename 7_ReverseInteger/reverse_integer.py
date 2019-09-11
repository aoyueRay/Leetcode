#-*- coding:utf-8 -*-

"""
Reverse digits of an integer.
Example1: x = 123, return 321
Example2: x = -123, return -321
"""

# 利用python的BIF，将整型转换为字符串后，反转字符串
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        temp = str(x)    # 将x转换为字符串
        symbol = ''    # 保存符号位，正数为空，负数为‘-’
        if x < 0:
            temp = temp[1:]    # 小于0时对符号位特殊处理
            symbol = '-'

        ans = temp[::-1]    # 将字符串反转（用python处理起来比较简单）
        ans = symbol + ans
        ans = int(ans)    # 反转后的字符串转化为整型

        # 处理反转后整数溢出的问题
        # int整形的取值范围为从-2^31(-2,147,483,648)到2^31-1(2,147,483,647)
        if (ans > 2 ** 31 -1) or (ans < -2 ** 31):
            return(0)
        else:
            return(ans)


# 利用整数的除法和取余处理
# ori源数据依次除以0,逐渐减少
# ret依次乘以10,逐渐增大
class Solution_1(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ori = abs(x)    # 取绝对值
        ret = 0    # 存放转换后的返回值
        while(ori != 0):
            ret = ret * 10 + ori % 10    # ret依次×10+余数
            ori = ori // 10    # ori依次除以10
        if (ret > 2 ** 31 - 1):
            return(0)    # int整型数据的取值范围处理
        if x < 0:
            return(0 - ret)    # 负数的处理
        return(ret)

if __name__ == '__main__':
    solution = Solution()
    x = -1000
    ans = solution.reverse(x)
    print(ans)