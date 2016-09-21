#-*- coding:utf-8 -*-

"""
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

"""

# 定义四个指针，分别移动指针，计算四个值的和，与target比较大小，进行判断。
# 主要移动后两个指针
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not nums:
            return([])    # 若输入列表为空，则返回空列表
        nums.sort()
        index_first = 0
        index_second = 0
        index_third = 0
        index_last = 0    # 定义四个指针分别指向四个索引
        answer = []    # 初始化返回列表

        for index_first in range(len(nums) - 3):
            index_second = index_first + 1
            index_third = index_second + 1
            index_last = len(nums) - 1
            while index_second < index_third and index_third < index_last:
                while index_third < index_last:
                    temp = nums[index_first] + nums[index_second] + nums[index_third] + nums[index_last]    # 计算一个临时值
                    if temp > target:
                        index_last -= 1    # 临时值大于目标值,则最后一个指针左移
                    elif temp < target:
                        index_third += 1    # 临时值大于目标值,则第三个指针右移
                    else:
                        temp_answer = [nums[index_first],nums[index_second],nums[index_third],nums[index_last]]    # 若值为目标值。，则保存该组合
                        if temp_answer not in answer:
                            answer.append(temp_answer)    # 避免重复解
                        index_third += 1
                index_second += 1    # 第二个指针前移一位
                index_third = index_second + 1    # 初始化第三个指针的位置
                index_last = len(nums) - 1    # 初始化最后一个指针的位置
        return(answer)



if __name__ == '__main__':
    solution = Solution()
    nums = [-3,-2,-1,0,0,1,2,3]
    target = 0
    ans = solution.fourSum(nums,target)
    print(ans)