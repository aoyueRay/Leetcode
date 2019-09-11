#-*- coding:utf-8 -*-

"""
 Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)

Note:
You can assume that you can always reach the last index.
"""

# 原本打算用递归算法，会造成超时。
# leetcode上一个极其牛逼的贪心算法
# 贪心算法的规则：在能够到达的范围之内，选择一个能够到达最远距离的点，更新步数，和更新最远到达的范围。
# 遍历列表中的点，算出当前能够到达的最大的索引位置，记为expect_max_index
# 其中每个点所能到达的最大的索引位置为each + nums[each]，each时每个点的索引
# already_max_index是从当前计数位置所能达到的最大的索引位置
# 当遍历的索引值大于already_max_index时，说明从当前计数位置没法到达最后位置，即需要更新步数
# 步数加一，且already_max_index更新为目前算出的预计最大的索引位置记为expect_max_index的值
# 依次类推，直到遍历到最后一个点，并返回所记录的步数
# 牛逼！
# Runtime = 128ms
class Solution(object):
    step_dict = {}    # 定义字典，避免重复计算
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        answer = 0    # 返回值
        expect_max_index = 0    # 预计能达到的最大索引值
        already_max_index = 0    # 已经到达的最大索引值
        for each in range(len(nums)):
            if each > already_max_index:    # 索引大于已达到的索引值时，更新数据
                already_max_index = expect_max_index    # 已达到最大索引更新为目前已经计算出来的预期最大索引值
                answer += 1     # 更新步数

            # 比较自身与当前位置所能到达的最大的索引位置，并更新预计能到达的最大索引值
            expect_max_index = max(expect_max_index,each + nums[each])
        return(answer)





if __name__ == '__main__':
    solution = Solution()
    nums = [2,3,1,1,4]
    nums = [2,3,0,1,4]
    nums = [6,2,6,1,7,9,3,5,3,7,2,8,9,4,7,7,2,2,8,4,6,6,1,3]
    ans = solution.jump(nums)
    print(ans)