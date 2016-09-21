#-*- coding:utf-8 -*-

"""
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?
"""

# 找到每个点转换前与转换后的对应关系，每次翻转都需要同时交换四个值
# 将转换过的值存在列表中，每次转换前都比对一下，若存在则不再进行转换。避免重复转换。
# 顺时针翻转90度时，每个点的对应规则：
# (row,column) -> (column,n - row - 1)
# (column,n - row - 1) -> (n - row - 1,n - column - 1)
# (n - row - 1,n - column - 1) -> (n - column - 1,row)
# (n - column - 1,row) -> (,row,column)
# Runtime = 64ms
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        print(matrix)
        n = len(matrix)
        if (not n) or (n == 1):
            return(matrix)
        dots = []    # 用于记录已经处理过的位置
        for row in range(n):
            for column in range(n):
                each_dot = (row,column)
                if each_dot not in dots:    # 检查该点是否已经经过转换
                    # 四个点的轮换
                    (matrix[row][column],matrix[column][n - row - 1],matrix[n - row - 1][n - column - 1],matrix[n - column - 1][row]) = \
                        (matrix[n - column - 1][row],matrix[row][column],matrix[column][n - row - 1],matrix[n - row - 1][n - column - 1])
                    dots.append((row,column))    # 将才与转换的点坐标加入到dots列表中
                    dots.append((column,n - row - 1))
                    dots.append((n - row - 1,n - column - 1))
                    dots.append((n - column - 1,row))
        return(matrix)

if __name__ == '__main__':
    solution = Solution()
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    ans = solution.rotate(matrix)
    print(ans)