#-*- coding:utf-8 -*-

"""
 Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.
"""

# 若采用递减的方式，由于数据太大，导致超时
# 即在递减的基础上，增加对除数（减数）的位处理，没减依次，左移一位，即除数（减数）翻倍
# 对应得到的差值1,需要按位转换后，才能得到对应的商值
# 可能出现超过int类型最大值的情况，需要单独处理
# 定义flag处理符号问题
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        MAX_INT = 2 ** 31 -1
        flag = True    # 定义符号标志，为True时返回正号，为False时返回负号
        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            flag = True
        else:
            flag = False
        quotient = 0    # 初始化商
        remainder = abs(dividend)    # 初始化余数，处理被除数的符号
        divisor = abs(divisor)    # 处理除数的符号
        while remainder >= divisor:
            reduced = divisor    # 重置减数，即在减数太大且大于当前的被减数时，重置减数为初始的除数
            temp = 0    # 初始化当次计算时差值1的位数
            while remainder >= reduced:
                remainder -= reduced    # 减法替换余数，商为递减的次数，先减一次，之后依次将除数按位移动翻倍
                quotient += (1 << temp)    # 每次减法的结果均为1,1的实际含义对应temp位数值
                temp += 1    # 每次计算后temp加一，即翻倍
                reduced <<= 1    # 减数左移一位，即翻倍
        if not flag:
            quotient = 0 - quotient    # 负号处理

        if quotient > MAX_INT:
            return(MAX_INT)    # 超过int类型的范围时，返回int类型的最大值
        else:
            return(quotient)



if __name__ == '__main__':
    solution = Solution()
    dividend = -2147483648
    divisor = -1
    ans = solution.divide(dividend,divisor)
    print(ans)