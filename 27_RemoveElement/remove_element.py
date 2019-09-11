#-*- coding:utf-8 -*-

"""
Given an array and a value, remove all instances of that value in place and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:
Given input array nums = [3,2,2,3], val = 3

Your function should return length = 2, with the first two elements of nums being 2.

Hint:

    Try two pointers.
    Did you use the property of "the order of elements can be changed"?
    What happens when the elements to remove are rare?

"""

# 56ms
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return(0)    # 处理长度为空的情况
        nums.sort()    # 排序，将val集中在一起
        val_count = nums.count(val)    # 计算val的个数
        if val_count == 0:
            return(len(nums))    # val为0,即val不在nums中的情况
        else:
            val_index = nums.index(val)    # 找到val的第一个位置
            del nums[val_index:val_index + val_count]    # 删除所有的val
            return(len(nums))


# 52ms
class Solution_1(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        length = len(nums)
        p = 0
        while (p < length):
            if nums[p] == val:    # 依次月val对比
                del nums[p]    # 与val相等，则删去
                length -= 1    # 长度减一
                p -= 1    # 索引值减一
            p += 1    # 若不相等，则索引加一

        return(length)


if __name__ == '__main__':
    solution = Solution()
    nums = [2]
    val = 3
    ans = solution.removeElement(nums,val)
    print(ans)