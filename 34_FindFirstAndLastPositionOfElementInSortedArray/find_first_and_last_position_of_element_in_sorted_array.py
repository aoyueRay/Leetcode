#-*- coding:utf-8 -*-

"""
Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
"""

# Runtime = 72ms
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1,-1]
        start = -1
        end = -1
        for i in range(len(nums)):
            if (nums[i] == target) and (start == -1):
                start = i    # 与target相等，且start为-1时，给start赋值
            if (nums[i] == target) and (start != -1):
                end = i    # 与target相等，且start不为-1时，给end赋值
        if (start != -1) and (end == -1):    # 只有一个匹配上的情况
            return([start,start])
        else:
            return([start,end])


# Runtime = 64ms
# 用python的index和count函数偷懒
class Solution_1(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return([-1,-1])    # nums为空的情况
        answer = []
        if target in nums:
            count = nums.count(target)
            start = nums.index(target)
            end = start + count - 1
            answer = [start,end]
        else:
            answer = [-1,-1]
        return(answer)


if __name__ == '__main__':
    solution = Solution()
    nums = [5, 7, 7, 8, 8, 10]
    nums = [2,2]
    target = 8
    target = 1
    ans = solution.searchRange(nums,target)
    print(ans)