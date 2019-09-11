#-*- coding:utf-8 -*-

"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character '.'.

You may assume that there will be only one unique solution.


A sudoku puzzle...


...and its solution numbers marked in red.
"""

# 如果把九宫格按照行从0开始标号，那么数字board[i][j] 位于第 i/3*3+j/3 个九宫格内
# 深度优先算法 + 回溯法
# 遍历数独，遇到'.'的情况，将1-9所有的情况替代'.'，并判断替代后的数独是否有效，以及替代后是否有可行解
# 若有则继续遍历并替代。
# 若没有则回溯并判断下一个点。
# Runtime = 1348ms
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.solve_sudoku(board)
        print(board)


    def solve_sudoku(self,board):
        for line in range(9):    # 遍历每行
            for column in range(9):    # 遍历每列
                if board[line][column] == '.':    # 遇到'.'时进行处理
                    for num in '123456789':    # 每个'.'都有可能为1-9中的数字
                        board[line] = board[line][:column] + num + board[line][column + 1:]
                        # board[line][column] = num    # 给'.'赋值
                        if self.judge_valid(line,column,board) and self.solve_sudoku(board):
                            return(True)    # 检查该点是否有效，有效则递归调用程序，检查数组是否有解，数组有解则返回True
                        # board[line][column] = '.'    # 无法确定该点的值，则将值回溯为'.'
                        board[line] = board[line][:column] + '.' + board[line][column + 1:]
                    return(False)    # 每个数字都不匹配，则返回False
        return(True)    # 数独中没有'.'存在，则返回True

    # 判断是否是有效的数独，只需要检查输入的点在行，列，子块中是否有重复
    # 输入：line（需检查的点的行索引），column（需检查的点的列索引），boadr（整个数独）
    # 输出：检查点无重复则返回True，有重复则数独无效返回False
    def judge_valid(self,line,column,board):
        comp = board[line][column]
        board[line] = board[line][:column] + '0' +board[line][column + 1:]    #修改检查点的值，避免检查时重复检查该点
        for each in range(9):
            if board[line][each] == comp:
                return(False)    # 检查所在行是否有相同数字，有则返回False
        for each in range(9):
            if board[each][column] == comp:
                return(False)    # 检查所在列是否有相同数字，有则返回False
        for each_line in range(3):
            for each_column in range(3):
                if board[line / 3 * 3 + each_line][column / 3 * 3 + each_column] == comp:
                    return(False)    # 检查所在方块是否有相同数字，又则返回False
        board[line] = board[line][:column] + comp + board[line][column + 1:]    # 还原赋值
        return(True)


# leetcode上Accepted的版本
class Solution_1(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def solve_sudoku(board):
            for line in range(9):    # 遍历每行
                for column in range(9):    # 遍历，没列
                    if board[line][column] == '.':    # 遇到'.'时进行处理
                        for num in '123456789':    # 每个'.'都有可能为1-9中的数字
                            board[line][column] = num    # 给'.'赋值
                            if judge_valid(line,column) and solve_sudoku(board):
                                return(True)    # 检查该点是否有效，有效则递归调用程序，检查数组是否有解，数组有解则返回True
                            board[line][column] = '.'    # 无法确定该点的值，则将值回溯为'.'
                        return(False)    # 每个数字都不匹配，则返回False
            return(True)    # 数独中没有'.'存在，则返回True

        # 判断是否是有效的数独，只需要检查输入的点在行，列，子块中是否有重复
        # 输入：line（需检查的点的行索引），column（需检查的点的列索引），boadr（整个数独）
        # 输出：检查点无重复则返回True，有重复则数独无效返回False
        def judge_valid(line,column):
            comp = board[line][column]
            board[line][column] = '0'    # 修改检查点的值，避免检查时重复检查该点
            for each in range(9):
                if board[line][each] == comp:
                    return(False)    # 检查所在行是否有相同数字，有则返回False
            for each in range(9):
                if board[each][column] == comp:
                    return(False)    # 检查所在列是否有相同数字，有则返回False
            for each_line in range(3):
                for each_column in range(3):
                    if board[line / 3 * 3 + each_line][column / 3 * 3 + each_column] == comp:
                        return(False)    # 检查所在方块是否有相同数字，又则返回False
            board[line][column] = comp
            return(True)

        solve_sudoku(board)



if __name__ == '__main__':
    solution = Solution()
    board = ['53..7....',
             '6..195...',
             '.98....6.',
             '8...6...3',
             '4..8.3..1',
             '7...2...6',
             '.6....28.',
             '...419..5',
             '....8..79']
    board = ["..9748...",
             "7........",
             ".2.1.9...",
             "..7...24.",
             ".64.1.59.",
             ".98...3..",
             "...8.3.2.",
             "........6",
             "...2759.."]
    board = [".....7..9",
             ".4..812..",
             "...9...1.",
             "..53...72",
             "293....5.",
             ".....53..",
             "8...23...",
             "7...5..4.",
             "531.7...."]
    board = ['8........',
             '..36.....',
             '.7..9.2..',
             '.5...7...',
             '....457..',
             '...1...3.',
             '..1....68',
             '..85...1.',
             '.9....4..']
    ans = solution.solveSudoku(board)
    print(ans)