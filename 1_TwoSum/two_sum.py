#-*- coding:utf-8 -*-

"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution.
Example:
    Given nums = [2, 7, 11, 15], target = 9,
    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i in range(len(nums)):
            dif = target - nums[i]    # 以列表中的元素为基数，做差，并检查这个差值是否在列表中
            if (dif in nums):
                indexb = nums.index(dif)    # 若差值在列表中，获取差值的索引值
                if indexb != i:    # 排除差值和基数是同一索引的情况
                    return([i,nums.index(dif)])
        return(None)

solution = Solution()
# nums = [2,7,11,15]
nums = [0,4,3,0]
# target = 9
target = 0
answer = solution.twoSum(nums,target)
print(answer)