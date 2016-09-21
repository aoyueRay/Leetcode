#-*- coding:utf-8 -*-

"""
 Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2,

with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the new length.
"""

# 176ms
class Solution_1(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return(0)    # nums为空时
        base_index = 0    # 基础指针，用于对比
        move_index = base_index + 1    # 移动指针
        while move_index < len(nums):
            if (nums[base_index] == nums[move_index]):
                del nums[move_index]    # 相等则删掉
            else:
                base_index = move_index    # 不想等则移动指针
                move_index += 1
        print(nums)
        return(len(nums))


# 92ms
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 0:
            return(0)    # 长度为空的处理
        compare = nums[0]    # 定义用于对比的元素
        data = 1    # data指向重复的那一个位置，若遇到不相等的，则替换该位置的数字
        for i in range(0,length):
            if nums[i] != compare:    # 遇到不相等的情况
                compare = nums[i]    # 修改用于对比的数字
                nums[data] = nums[i]    # 将重复的元素替换为不重复的那个
                data += 1    # data指针后移
        return(data)


if __name__ == '__main__':
    solution = Solution()
    nums = [1]
    ans = solution.removeDuplicates(nums)
    print(ans)