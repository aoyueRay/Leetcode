#-*- coding:utf-8 -*-

"""
Given an array S of n integers,
find three integers in S such that the sum is closest to a given number, target.
Return the sum of the three integers.
You may assume that each input would have exactly one solution.

For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""

# 定义三个坐标，从左右两边同时往中间判断。
# 可以避免部分的重复计算
# 先排序，begin指向的基数，移动middle和end。
# 计算的临时值大于target，则移动end使其值减小
# 计算的临时值小于target，则移动middle使值变大
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return(0)
        begin = 0    # 初始化指针
        middle = 0    # 初始化指针
        end = 0    # 初始化指针
        temp = 0    # 初始化中间值变量保存临时结果
        nums.sort()    # 排序
        answer = nums[0] + nums[1] + nums[2]  # 初始化返回值
        print(nums)
        for begin in range(len(nums) - 2):
            middle = begin + 1    # 中间指针初始为起始指针的下一个位置
            end = len(nums) - 1    # 末尾指针初始为最后一个位置
            while middle < end:
                temp = nums[begin] + nums[middle] + nums[end]
                print('-' * 20)
                print('temp->',temp)
                print('answer->',answer)
                if abs(target - temp) < abs(target - answer):
                    answer = temp    # 距离target近的值保存在answer中
                if temp < target:
                    middle += 1    # temp小于target，则中间指针往后移一位
                elif temp > target:
                    end -= 1    # temp大于target，则尾指针往前移一位
                else:
                    middle += 1
                    end -= 1    # 否则两边指针同时移位
                print('answer--->',answer)
        return(answer)


# 通过暴力解法，算出三个数的和，然后对比target，算出其和与target最接近的一个解
# 解法超时，不可取
class Solution_1(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 4:
            return(sum(nums))    # 若列表元素小于等于3个，返回三个元素的和
        index_1 = 0    # 初始化第1个数的索引
        index_2 = 0    # 初始化第2个数的索引
        index_3 = 0    # 初始化第3个数的索引
        total = sum(nums[:3])    # 初始化三个数的和
        dif = abs(target - sum(nums[:3]))    # 初始化差值
        minimum = dif    # 初始化最小差值
        answer = nums[:3]    # 初始化列表保存最小差值的组合
        while index_1 < len(nums):
            index_2 = index_1 + 1
            while index_2 < len(nums):
                index_3 = index_2 + 1
                while index_3 < len(nums):
                    total = nums[index_1] + nums[index_2] + nums[index_3]
                    dif = abs(target - total)
                    if dif < minimum:
                        minimum = dif
                        answer = [nums[index_1],nums[index_2],nums[index_3]]
                    index_3 += 1
                index_2 += 1
            index_1 += 1
        print(answer)
        return(sum(answer))



if __name__ == '__main__':
    solution = Solution()
    nums = [1,-3,3,5,4,1]
    target = 1
    ans = solution.threeSumClosest(nums,target)
    print(ans)