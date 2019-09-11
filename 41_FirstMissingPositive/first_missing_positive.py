#-*- coding:utf-8 -*-

"""
 Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
"""

# 交换数组元素，使得数组中第i位存放数值(i+1)。
# 最后遍历数组，寻找第一个不符合此要求的元素，返回其下标。
# 整个过程需要遍历两次数组，复杂度为O(n)。
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:    # nums为空的情况
            return(1)
        init_index = 0
        while init_index < len(nums):
            # 交换条件：实际值与理论值不相等，且实际值大于等于0,且需要交换的索引大于等于0,
            # 且交换的索引小于列表长度，且实际值与需要交换的值不相等
            if (nums[init_index] != init_index + 1) and (nums[init_index] >= 0) and (nums[init_index] - 1 >= 0) and \
                    (nums[init_index] - 1 < len(nums)) and (nums[init_index] != nums[nums[init_index] - 1]):
                swap_index = nums[init_index] - 1
                nums[init_index],nums[swap_index] = nums[swap_index],nums[init_index]
                init_index -= 1    # 交换后指针索引减一
                print('交换一次')
            init_index += 1

        for each_index in range(len(nums)):
            if nums[each_index] != each_index + 1:
                answer = each_index + 1
                break
            else:
                answer = nums[each_index] + 1
        return(answer)



if __name__ == '__main__':
    solution = Solution()
    nums = [3,4,-1,1]
    nums = [0,1,2]
    ans = solution.firstMissingPositive(nums)
    print(ans)