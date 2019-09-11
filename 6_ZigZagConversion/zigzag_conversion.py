#-*- coding:utf-8 -*-


"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:
string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
"""

# 根据numRows定义一个程度相等的列表，列表的每一项分别，每一行对应的是转换后的字符串。
# 依次读字符串中的字符，判断其在哪一行，并以该行号为索引，添加到上述的列表中
# 最后将列表中的字符串整合为一个字符串返回即可
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        output = ''    # 初始化返回值字符串
        ans = []    # 对应每个下标，存放每一行的字符串
        for i in range(numRows):
            ans.append('')    # 根据行数初始化列表
        each_index = 0    # 对应每个字符在字符串中的索引值，依次递增
        if not s or numRows <= 0:
            return(‘’)    # 字符串为空或行数小于0时的处理
        if numRows == 1:
            return(s)    # 行数为1时返回其本身
        while each_index < len(s):
            column = each_index / (numRows - 1)    # 列参数
            if column % 2 :
                line = (column + 1) * (numRows - 1) - each_index    # 列参数为奇数时，计算其所在的行号
            else:
                line = each_index % (numRows - 1)    # 列参数为偶数时，计算其所在的行号
            ans[line] = ans[line] + s[each_index]    # 将字符添加到列表对应位置的字符串中
            each_index += 1    # 字符索引递增
        for each in range(numRows):
            output = output + ans[each]    # 将列表中的字符串整合为一个字符串
        return(output)



if __name__ == '__main__':
    solution = Solution()
    s = 'PAYPALISHIRING'
    numRows = 3
    ans = solution.convert(s,numRows)
    print(ans)