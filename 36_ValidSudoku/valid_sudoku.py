#-*- coding:utf-8 -*-

"""
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.


Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.

Subscribe to see which companies asked this question

"""


# 分别判断数独中每行，没列以及每块中是否有重复元素
# 对重复元素的判断参考RemoveDuplicatesFromSortedArray的算法
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        print(board)

        for row_index in range(len(board)):
            # 检查数独的每一行
            row_list = []
            row_list.append(board[row_index])
            # print('按行判断。。。')
            row_flag = self.judge_duplicates(row_list)
            if not row_flag:    # 检查包含有重复元素，则返回False
                return(False)

            # 检查数独的每一列
            column_list = []
            column_str = ''
            for each_index in range(len(board)):
                column_str += board[each_index][row_index]
            column_list.append(column_str)
            # print('按列判断。。。')
            colunm_flag = self.judge_duplicates(column_list)
            if not colunm_flag:    # 检查包含有重复元素，则返回False
                return(False)

        # 检查数独的每个小方块
        for squre_column in range(0,9,3):
            for squre_row in range(0,9,3):
                squre_list = []
                squre_str = ''
                for each_squre_column in range(squre_column,squre_column + 3):
                    for each_squre_row in range(squre_row,squre_row + 3):
                        squre_str += board[each_squre_column][each_squre_row]
                squre_list.append(squre_str)
                # print('按块判断。。。')
                squre_flag = self.judge_duplicates(squre_list)
                if not squre_flag:
                    return(False)
        return(True)


    # 检查列表中是否有重复元素，算法参考RemoveDuplicatesFromSortedArray
    # 输入：列表
    # 输出：flag标志，为True时表示没有重复，False时表示存在重复元素
    def judge_duplicates(self, lists):
        nums = lists[:]
        nums = list(nums[0])
        nums.sort(reverse=True)    # 将列表逆序排列，即将'.'排列在最后
        if '.' in nums:    # '.'存在的处理
            dot_index = nums.index('.')    # 找到'.'的初始索引位置
            nums = nums[:dot_index]    # 将含有'.'的部分删去
        length = len(nums)
        if length == 0:    # 全是'.'时，返回True
            return(True)
        compare = nums[0]  # 定义用于对比的元素
        data = 1  # data指向重复的那一个位置，若遇到不相等的，则替换该位置的数字
        for i in range(0, length):
            if nums[i] != compare:  # 遇到不相等的情况
                compare = nums[i]  # 修改用于对比的数字
                nums[data] = nums[i]  # 将重复的元素替换为不重复的那个
                data += 1  # data指针后移
        if data == len(nums):    # 无重复元素
            return(True)
        else:
            return(False)



if __name__ == '__main__':
    solution = Solution()
    board = [".87654321",
             "2........",
             "3........",
             "4........",
             "5........",
             "6........",
             "7........",
             "8........",
             "9........"]
    board = ["..4...63.",
             ".........",
             "5......9.",
             "...56....",
             "4.3.....1",
             "...7.....",
             "...5.....",
             ".........",
             "........."]
    board = ['812753649', '943612857', '675498213', '354287196', '169345782', '287169534', '521974368', '438526971.', '796831425']
    ans = solution.isValidSudoku(board)
    print(ans)