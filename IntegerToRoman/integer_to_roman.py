#-*- coding:utf-8 -*-

"""
Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.
"""

# I-1
# -V-5
# X-10
# L-50
# C-100
# D-500
# M-1000
# 以1000,900,500,400....5,4,1分别为分割节点进行个数的计算
# divmod(num1,num2)返回(商,余数)的元组
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        output = ''    # 初始化返回值

        (count_m,num) = divmod(num,1000)    # 计算M的个数
        output = output + 'M' * count_m

        (count_cm,num) = divmod(num,900)    # 计算CM的个数
        output = output + 'CM' * count_cm

        (count_d, num) = divmod(num,500)  # 计算D的个数
        output = output + 'D' * count_d

        (count_cd, num) = divmod(num,400)  # 计算CD的个数
        output = output + 'CD' * count_cd

        (count_c, num) = divmod(num,100)  # 计算C的个数
        output = output + 'C' * count_c

        (count_xc, num) = divmod(num,90)  # 计算XC的个数
        output = output + 'XC' * count_xc

        (count_l, num) = divmod(num,50)  # 计算L的个数
        output = output + 'L' * count_l

        (count_xl, num) = divmod(num,40)  # 计算XL的个数
        output = output + 'XL' * count_xl

        (count_x, num) = divmod(num,10)  # 计算X的个数
        output = output + 'X' * count_x

        (count_ix, num) = divmod(num,9)  # 计算IX的个数
        output = output + 'IX' * count_ix

        (count_v, num) = divmod(num,5)  # 计算V的个数
        output = output + 'V' * count_v

        (count_iv, num) = divmod(num,4)  # 计算IV的个数
        output = output + 'IV' * count_iv

        (count_i, num) = divmod(num,1)  # 计算I的个数
        output = output + 'I' * count_i

        return(output)

if __name__ == '__main__':
    solution = Solution()
    num = 1976
    ans = solution.intToRoman(num)
    print(ans)