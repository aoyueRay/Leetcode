#-*- coding:utf-8 -*-

"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0
"""

# Runtime = 72ms
# 不使用python的BIF
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return(0)    # nums为空的情况
        if target <= nums[0]:
            return(0)    # 小于最小值的情况
        if target > nums[-1]:
            return(len(nums))    # 大于最大值的情况
        start = 0
        end = 0
        while start < len(nums) - 1:
            end = start + 1    # 定义相邻两个指针
            if (nums[start] < target) and (nums[end] >= target):    # 找target在两个指针之间的情况
                return(end)
            start += 1

# Runtime = 72ms
# 用python的index()函数偷懒。。。
class Solution_1(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return(0)    # nums为空的情况
        nums.append(target)    # 将target添加到列表中
        nums.sort()    # 列表排序
        answer = nums.index(target)    # 找到target的索引值
        return(answer)



if __name__ == '__main__':
    solution = Solution()
    nums = [1,3,5]
    target = 4
    ans = solution.searchInsert(nums,target)
    print(ans)