#-*- coding:utf-8 -*-

"""
Implement atoi to convert a string to an integer.
Hint: Carefully consider all possible input cases.
If you want a challenge, please do not see below and ask yourself what are the possible input cases.
Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.
"""

# ord()将字符转换为ascii码
# chr()将ascii码转换为字符
# '+'的ascii码为43
# '-'的ascii码为45
# '0'的ascii码为48
# 整型数据的范围为：-2^31到2^31-1
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if not str:
            return(0)    # 字符串为空时返回0

        str = str.strip()    #处理字符串中可能出线的空字符
        temp = str[:]  # 拷贝一个新的字符串用于操作

        answer = 0    # 定义返回值，初始化为0
        if (ord(temp[0]) == 45) or (ord(temp[0]) == 43):
            temp = temp[1:]    # 若第一位为'+'或者'-'时，去掉符号位
        for i in range(len(temp)):
            each_num = ord(temp[i]) - 48    # 将字符转化为数字，其中0的ascii码为48
            if each_num not in range(10):
                break    # 若字符串中含有非数字字符，则表示异常，跳出循环，返回当前的数字
            else:
                answer = answer * 10 + each_num    # 依次乘以10，进位处理

        # 对于超过整型范围的值的处理
        if ord(str[0]) == 45:
            answer = 0 - answer
        if answer > 2 ** 31 - 1:
            return(2 ** 31 - 1)    # 整型数据的边界处理，最大为2^31-1,大于最大值则返回最大值
        elif answer < -2 ** 31:
            return(-2 ** 31)    # 整型数据的边界处理，最小为-2^31，小于最小值则返回最小值
        else:
            return(answer)



if __name__ == "__main__":
    solution = Solution()
    str = "     -00100a11"
    ans = solution.myAtoi(str)
    print(ans)