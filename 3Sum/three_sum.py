#-*- coding:utf-8 -*-

"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        great = []
        less = []
        answers = []

        # 处理元素0个数大于等于3的情况
        if nums.count(0) > 2:
            answers = [[0, 0, 0]]

        # 将原列表拆分为大于0或者小于等于0的两个列表
        for each_num in nums:
            if each_num > 0:
                great.append(each_num)
            else:
                less.append(each_num)

        # 全大于0或者全小于0的时候返回空
        if (not great) or (not less):
            return(answers)

        # 排序处理结果重复的情况
        great.sort()
        less.sort()

        answers.extend(self.findOpposite(great,less))
        answers.extend(self.findOpposite(less,great))
        return(answers)

    # 计算列表中两个元素的和以及对应的相反数，并在另一个列表中查找该相反数是否存在
    # 若存在则作为结果返回
    # 若不存在则跳过判断下一组数据
    def findOpposite(self,list_add,list_result):
        init_index = 0    # 初始化基础指针，指向其中一个加数
        move_index = 0    # 初始化移动指针，指向另一个加数
        answers = []
        while init_index < len(list_add) - 1:
            move_index = init_index + 1
            while move_index < len(list_add):
                target = 0 - (list_add[init_index] + list_add[move_index])    # 计算目标值
                if target in list_result:
                    each_answer = []    # 初始化列表，若目标值存在在列表中，则加入返回值列表
                    each_answer.append(list_add[init_index])
                    each_answer.append(list_add[move_index])
                    each_answer.append(target)

                    # 去除重复的结果
                    if each_answer not in answers:
                        answers.append(each_answer)    # 将结果添加到返回列表中
                move_index += 1
            init_index += 1
        return(answers)


if __name__ == '__main__':
    solution = Solution()
    nums = [0,0,0,0]
    ans = solution.threeSum(nums)
    print(ans)