#-*- coding:utf-8 -*-

"""
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.
"""


# 遍历列表，找到与target相等的数，返回索引值，否则返回-1
# Runtime = 48ms
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        init_index = 0
        answer = -1    # 初始化返回值
        while init_index < len(nums):
            if nums[init_index] == target:    # 找到与target相等的数
                answer = init_index    # 返回索引值
                break    # 跳出循环
            else:
                init_index += 1
        return(answer)



# 用pyhton list的BIF index()可以直接解决
# Runtime = 56ms
class Solution_1(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        answer = -1    # 初始化返回值，默认找不到
        if target in nums:
            answer = nums.index(target)    # 找到则返回对应的索引
        return(answer)


if __name__ == '__main__':
    solution = Solution()
    nums = [4,5,6,7,0,1,2]
    target = 7
    ans = solution.search(nums,target)
    print(ans)