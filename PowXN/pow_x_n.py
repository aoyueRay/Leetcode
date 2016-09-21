#-*- coding:utf-8 -*-

"""
Implement pow(x, n).
"""



# 用while循环计数，flag判断n的符号
# 通过二分的方法，n为偶数时，将x转换为x*x
# Runtime = 60ms
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:    # 幂为0的情况
            return(1.0)
        flag = True    # 符号标志，n为正时为True，n为负时为False
        answer = 1
        if n < 0:
            n = -n
            flag = False
        while n > 0:
            if n % 2 == 1:    # n为奇数时
                answer = answer * x
            x *= x
            n /= 2
        if not flag:    # 幂次为负数时取导数
            answer = 1.0 / answer
        return(answer)



# 利用python的幂运算符**
# Runtime = 56ms
class Solution_1(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        return(x ** n)


if __name__ == '__main__':
    solution = Solution()
    x = 3.2
    x = 34.00515
    x = 8.88023
    n = 3
    ans = solution.myPow(x,n)
    print(ans)