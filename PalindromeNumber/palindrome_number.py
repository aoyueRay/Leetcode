#-*- coding:utf-8 -*-

"""
Determine whether an integer is a palindrome. Do this without extra space.
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return(False)    # 负数不是回文数
        origin = x    # 临时变量保存x
        answer = 0    # 定义变量，保存x的逆序

        # 将x逆序保存在answer中
        while x != 0:
            answer = answer * 10 + x % 10    # answer乘以10加上x模10的余数
            x = x / 10    # 去掉最低位
        # 对比源数字与逆序后的数字是否相等，相等则为回文数
        if answer == origin:
            return(True)
        else:
            return(False)


if __name__ == '__main__':
    solution = Solution()
    x = 1000021
    ans = solution.isPalindrome(x)
    print(ans)