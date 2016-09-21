# -*- coding:utf-8 -*-

"""
 Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

"""

# 题意是，查找比当前序列大的下一个序列，若不存在，则按升序返回
# 下面这种算法据说是STL中的经典算法。
# 在当前序列中，从尾端往前寻找两个相邻升序元素，升序元素对中的前一个标记为partition。
# 然后再从尾端寻找另一个大于partition的元素，并与partition指向的元素交换，
# 然后将partition后的元素（不包括partition指向的元素）逆序排列。
# 比如14532，那么升序对为45，partition指向4。
# 由于partition之后除了5没有比4大的数，所以45交换为54，即15432.
# 然后将partition之后的元素逆序排列，即432排列为234，则最后输出的next permutation为15234。
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return([])

        index = len(nums) - 2    # 定位到倒数第二个位置
        while index >= 0 and (nums[index] >= nums[index + 1]):
            index -= 1    # 找到升序元素，定位partition
        partition = index
        if partition == -1:
            return(nums[::-1])    # nums为最大序列时，返回其最小序列
        swap_index = len(nums) - 1
        while swap_index >= 0:
            if nums[swap_index] > nums[partition]:
                nums[swap_index],nums[partition] = nums[partition],nums[swap_index]    # 交换位置
                break
            else:
                swap_index -= 1
        nums[partition + 1:] = nums[(partition + 1):][::-1]    # 将partition后的部分逆序排列
        return(nums)



if __name__ == '__main__':
    solution = Solution()
    nums = [1,2,3,4,5,6]
    nums = [5,3,4,2,1]
    nums = [1,5,1]
    # nums = [1]
    # nums = [3,2,1]
    ans = solution.nextPermutation(nums)
    print(ans)